import cv2
import numpy
import utils
from sklearn.cluster import MiniBatchKMeans


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

    def _edge_detect(self):
        image = cv2.imread(self.image_path)
        gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
        edged = cv2.Canny(blurred, 0, 100, apertureSize=3)
        return edged

    def _quantify_colors(self):
        image = cv2.imread(self.image_path)
        (h, w) = image.shape[:2]
        image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        image = image.reshape((image.shape[0] * image.shape[1], 3))
        clt = MiniBatchKMeans(n_clusters=8)
        labels = clt.fit_predict(image)
        quantified = clt.cluster_centers_.astype('uint8')[labels]
        quantified = quantified.reshape((h, w, 3))
        return cv2.cvtColor(quantified, cv2.COLOR_LAB2BGR)

    def _get_ref_point_width(self):
        image = self._quantify_colors()
        upper_bound = numpy.array([75, 75, 255])
        lower_bound = numpy.array([0, 0, 130])
        mask = cv2.inRange(image, lower_bound, upper_bound)
        marker = cv2.bitwise_and(image, image, mask=mask)
        marker = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(marker, cv2.cv.CV_HOUGH_GRADIENT, 3, 200)
        ref_point = circles[0][0]
        if self.debug:
            utils.debug_print(self.__class__.__name__, '_get_ref_point_width', ref_point[2] * 2.0)
        return ref_point[2] * 2.0

    def _get_measurement_px(self):
        min_line_length = 300
        max_line_gap = 10
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
                            y2 <= ((image_height / 3) * 2) and \
                            abs(x1 - x2) <= 1:
                y_min = min(y_min, y1)
                y_max = max(y_max, y2)

        if self.debug:
            utils.debug_print(self.__class__.__name__, '_get_measurement_px', y_max - y_min)
        return y_max - y_min

    def _convert_px_mm(self, measurement_px):
        self.pixels_per_mm = self._get_ref_point_width() / self.REF_POINT_KNOWN_WIDTH
        if self.debug:
            utils.debug_print(self.__class__.__name__, '_convert_px_mm', self.pixels_per_mm)
        return measurement_px / self.pixels_per_mm

    def get_measurement(self, image_path):
        self.image_path = image_path
        print image_path
        self.processed_image = self._edge_detect()
        measurement_px = self._get_measurement_px()
        measurement_mm = self._convert_px_mm(measurement_px)

        if self.debug:
            utils.debug_print(self.__class__.__name__, 'get_measurement', measurement_mm)

        return measurement_mm
