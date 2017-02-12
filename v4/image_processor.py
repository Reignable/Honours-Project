import cv2
import numpy


def show_image(image, wait_time):
    """
    Displays the given image in a window
    :param wait_time:
    :param image: The image to display
    :return: None
    """
    try:
        cv2.imshow(str(image), image)
        cv2.waitKey(wait_time)
        return 0
    except cv2.error as e:
        print e.message


class ImageProcessor:
    image_path = None
    processed_image = None
    sag = None
    pressure = None
    stroke = None
    pixels_per_mm = None
    debug_mode = False

    def __init__(self, image_path, sag, pressure, stroke, debug=False):
        self.image_path = image_path
        self.sag = sag
        self.pressure = pressure
        self.stroke = stroke
        self.debug_mode = debug

    def _process_image(self):
        """
        Applies the appropriate processes before analysis can be carried out
        :return: The processed image with edge detection applied
        """
        image = cv2.imread(self.image_path)
        gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
        edged = cv2.Canny(blurred, 0, 100, apertureSize=3)
        return edged

    def _get_ref_point_width(self):
        """
        Locate red circle in image and output its diameter in px
        :return:
        """
        image = cv2.imread(self.image_path)
        upper_bound = numpy.array([65, 65, 255])
        lower_bound = numpy.array([0, 0, 200])
        mask = cv2.inRange(image, lower_bound, upper_bound)
        marker = cv2.bitwise_and(image, image, mask=mask)
        marker = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(marker, cv2.cv.CV_HOUGH_GRADIENT, 3, 200)
        ref_point = circles[0][0]
        return ref_point[2] * 2.0

    def _get_measurement_px(self):
        """
        Measures the distance between the shock body and o-ring in pixels
        :return: The measurement in px
        """
        if self.processed_image is None:
            self.processed_image = self._process_image()
        min_line_length = 300
        max_line_gap = 1
        image_height, image_width = self.processed_image.shape[:2]
        y_min = image_height
        y_max = 0
        lines = cv2.HoughLinesP(self.processed_image,
                                1,
                                numpy.pi / 180,
                                50,
                                min_line_length,
                                max_line_gap)
        for x1, y1, x2, y2 in lines[0]:
            if x1 >= image_width / 2 and \
                            y1 >= image_height / 3 and \
                            y2 <= (image_height * 0.45) and \
                            abs(x1 - x2) <= 1:
                y_min = min(y_min, y1)
                y_max = max(y_max, y2)
        return y_max - y_min

    def _get_measurement_mm(self, measurement_px):
        if self.pixels_per_mm is None:
            self.pixels_per_mm = self._get_ref_point_width() / 5
        return measurement_px / self.pixels_per_mm

    def _get_inverse_measurement(self, measurement_mm):
        return self.stroke - measurement_mm

    def _get_psi_per_mm(self, measurement_mm):
        return self.pressure / measurement_mm

    def _get_ideal_sag_mm(self):
        return self.stroke - (float(self.stroke) * (float(self.sag) / 100.0))

    def calc_ideal_pressure(self):
        pixels_per_mm = self._get_ref_point_width() / 5
        measurement_px = self._get_measurement_px()
        measurement_mm = measurement_px / pixels_per_mm
        inverse_mm = self._get_inverse_measurement(measurement_mm)
        psi_per_mm = self._get_psi_per_mm(inverse_mm)
        ideal_mm = self._get_ideal_sag_mm()
        ideal_psi = psi_per_mm * ideal_mm
        if self.debug_mode:
            print 'px/mm', pixels_per_mm
            print 'measurement_px', measurement_px
            print 'measurement_mm', measurement_mm
            print 'desired mm', ideal_mm
            print 'psi_per_mm', psi_per_mm

        return ideal_psi
