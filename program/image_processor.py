import cv2
import numpy

import sys

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
    REF_POINT_KNOWN_WIDTH = 9.5

    image_path = None
    edged_image = None
    quantified_image = None
    pixels_per_mm = None
    debug = False
    ref_point = None
    oring = None
    colour = None

    def __init__(self, colour='red', debug=False):
        self.colour = colour
        self.debug = debug

    def _edge_detect(self):
        image = cv2.imread(self.image_path)
        gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
        edged = cv2.Canny(blurred, 10, 90, apertureSize=3)
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

    def _find_red(self):
        image = self._quantify_colors()
        self.quantified_image = image
        upper_bound = numpy.array([100, 100, 255])
        lower_bound = numpy.array([0, 0, 130])
        mask = cv2.inRange(image, lower_bound, upper_bound)
        marker = cv2.bitwise_and(image, image, mask=mask)
        marker = cv2.cvtColor(marker, cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(marker.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        return sorted(contours, key=cv2.contourArea, reverse=True)[:2]

    def _find_ref(self):
        try:
            self.ref_point = self._find_red()[0]
        except (ValueError, IndexError):
            print 'Could not find reference point\n' \
                  'Is the the correct colour given and is one present in the image?\nIf ' \
                  'yes, please try again.'
            sys.exit(1)

    def _find_oring(self):
        if self.colour == 'red':
            try:
                self.oring = self._find_red()[1]
            except IndexError:
                print 'Could not find o-ring\n'\
                      'Is the the correct colour given and is one present in the image?\nIf ' \
                      'yes, please try again.'
                sys.exit(1)
        elif self.colour == 'black':
            image = cv2.imread(self.image_path)
            (height, width) = image.shape[:2]
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            (T, thresh) = cv2.threshold(gray, 30, 150, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
            for contour in contours:
                _, y, _, _ = cv2.boundingRect(contour)
                if y > (height / 3):
                    self.oring = contour

    def _get_ref_point_width(self):
        (_, _), radius = cv2.minEnclosingCircle(self.ref_point)
        if self.debug:
            utils.debug_print(self.__class__.__name__, '_get_ref_point_width', radius * 2)
        return radius * 2

    def _get_oring_height(self):
        _, y, _, h = cv2.boundingRect(self.oring)
        if self.debug:
            utils.debug_print(self.__class__.__name__, '_get_oring_height', y+h)
        return y + h

    def _get_measurement_px(self):
        min_line_length = 1000
        max_line_gap = 10
        image_height, image_width = self.edged_image.shape[:2]
        y_limit = self._get_oring_height()
        y_min = image_height
        y_max = 0
        lines = cv2.HoughLinesP(self.edged_image,
                                1,
                                numpy.pi / 180,
                                50,
                                min_line_length,
                                max_line_gap)
        for x1, y1, x2, y2 in lines[0]:
            if x1 >= image_width / 2 and \
                            y1 >= image_height / 3 and \
                            y2 <= y_limit and \
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
        if self.debug:
            utils.debug_print(self.__class__.__name__, 'filepath', self.image_path)
        self.edged_image = self._edge_detect()
        self._find_ref()
        self._find_oring()
        measurement_px = self._get_measurement_px()
        measurement_mm = self._convert_px_mm(measurement_px)

        if self.debug:
            utils.debug_print(self.__class__.__name__, 'get_measurement', measurement_mm)
        if measurement_mm <= 0:
            print 'Incorrect measurement produced from image {i}\n'\
                  'Please check settings and try again.'.format(i=self.image_path)
            sys.exit(1)
        return measurement_mm
