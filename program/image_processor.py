import cv2
import numpy


def show_image(image, wait_time):
    try:
        cv2.imshow(str(image), image)
        cv2.waitKey(wait_time)
        return 0
    except cv2.error as e:
        print e.message


class ImageProcessor:
    REF_POINT_KNOWN_WIDTH = 7.5
    image_path = None
    processed_image = None
    pixels_per_mm = None
    debug = False

    def __init__(self, debug=False):
        self.debug = debug

    def _process_image(self):
        image = cv2.imread(self.image_path)
        gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
        edged = cv2.Canny(blurred, 0, 100, apertureSize=3)
        return edged

    def _get_ref_point_width(self):
        image = cv2.imread(self.image_path)
        upper_bound = numpy.array([65, 65, 255])
        lower_bound = numpy.array([0, 0, 200])
        mask = cv2.inRange(image, lower_bound, upper_bound)
        marker = cv2.bitwise_and(image, image, mask=mask)
        marker = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(marker, cv2.cv.CV_HOUGH_GRADIENT, 3, 200)
        ref_point = circles[0][0]
        if self.debug:
            print 'ImgPro:_get_ref_point_width:', ref_point[2] * 2.0
        return ref_point[2] * 2.0

    def _get_measurement_px(self):
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

        if self.debug:
            print 'ImgPro:_get_measurement_px:', y_max - y_min
        return y_max - y_min

    def _convert_px_mm(self, measurement_px):
        self.pixels_per_mm = self._get_ref_point_width() / self.REF_POINT_KNOWN_WIDTH
        return measurement_px / self.pixels_per_mm

    def get_measurement(self, image_path):
        self.image_path = image_path
        print image_path
        self.processed_image = self._process_image()
        measurement_px = self._get_measurement_px()
        measurement_mm = self._convert_px_mm(measurement_px)

        if self.debug:
            print 'ImgPro:get_measurement_mm:', measurement_mm

        return measurement_mm
