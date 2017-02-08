import cv2
import numpy

args = None
op_sensor_height = 4.921
pixels_per_mm = None


class Thing:
    def __init__(self):
        pass

    def show_image(self, image):
        """
        Displays the given image in a window
        :param image: The image to display, cv2.Mat
        :return: None
        """
        cv2.imshow(str(image), image)
        cv2.waitKey(0)
        return 0

    def process_image(self, image_path):
        """
        Applies the appropriate processes before analysis can be carried out
        :param image_path: File-path to the image to be processed
        :return: The processed image with edge detection applied
        """
        image = cv2.imread(image_path)
        gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
        edged = cv2.Canny(blurred, 0, 100, apertureSize=3)
        return edged

    def get_ref_point_width(self, image_path):
        """
        Locate red circle in image and output its diameter in px
        :param image_path:
        :return:
        """
        image = cv2.imread(image_path)
        upper_bound = numpy.array([65, 65, 255])
        lower_bound = numpy.array([0, 0, 200])
        mask = cv2.inRange(image, lower_bound, upper_bound)
        marker = cv2.bitwise_and(image, image, mask=mask)
        marker = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(marker, cv2.cv.CV_HOUGH_GRADIENT, 3, 200)
        ref_point = circles[0][0]
        return ref_point[2] * 2

    def get_measurement_px(self, image):
        """
        Measures the distance between the shock body and o-ring in pixels
        :param image: The image to measure
        :return: The measurement in px
        """
        min_line_length = 300
        max_line_gap = 1
        image_height, image_width = image.shape[:2]
        y_min = image_height
        y_max = 0
        lines = cv2.HoughLinesP(image, 1, numpy.pi / 180, 50, min_line_length, max_line_gap)
        for x1, y1, x2, y2 in lines[0]:
            if (x1 >= image_width / 2
                and y1 >= image_height / 3
                and y2 <= (image_height * 0.45)
            and abs(x1 - x2) <= 1):
                y_min = min(y_min, y1)
                y_max = max(y_max, y2)
        return y_max - y_min

    def get_measurement_mm(self, measurement_px):
        global pixels_per_mm
        if pixels_per_mm is None:
            pixels_per_mm = self.get_ref_point_width(args.image) / 5
        return measurement_px / pixels_per_mm

    def get_mm_per_psi(self, measurement_mm):
        return measurement_mm / args.pressure

    def calc_ideal_pressure(self, mm_per_psi):
        # work out ideal mm, sag percentage of shock travel
        ideal_mm = float(args.stroke) * ((100.0 - float(args.sag)) / 100.0)
        # work out psi for that measurement
        return ideal_mm * mm_per_psi


