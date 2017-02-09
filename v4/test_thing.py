import cv2
from unittest import TestCase
from image_processor import ImageProcessor

'''
assertEqual()
assertTrue()
assertFalse()
assertRaises()
'''


class TestImageProcessor(TestCase):

    image_processor = None
    processed_test_image = None

    def setUp(self):
        global image_processor
        image_processor = ImageProcessor()
        image = cv2.imread('test_image.jpg')
        gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
        global processed_test_image
        processed_test_image = cv2.Canny(blurred, 0, 100, apertureSize=3)

    def tearDown(self):
        pass

    def test_show_image_normal(self):
        try:
            image = cv2.imread('test_image.jpg')
            result = image_processor.show_image(image)
            self.assertEqual(result, 0)
        except cv2.error as e:
            self.fail('show_image() raised exception\n'+e.message)

    def test_process_image_normal(self):
        processed_image = image_processor.process_image('test_image.jpg')
        self.assertEqual(processed_image.all(), processed_test_image.all())

    def test_get_ref_point_width_normal(self):
        pass

    def test_get_measurement_px_normal(self):
        pass

    def test_get_measurement_mm_normal(self):
        pass

    def test_get_mm_per_psi_normal(self):
        pass

    def test_calc_ideal_pressure_normal(self):
        pass
