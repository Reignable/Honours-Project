import cv2
from unittest import TestCase
from thing import Thing

'''
assertEqual()
assertTrue()
assertFalse()
assertRaises()
'''


class TestThing(TestCase):

    image_processor = None

    def setUp(self):
        global image_processor
        image_processor = Thing()

    def tearDown(self):
        pass

    def test_show_image(self):
        try:
            image = cv2.imread('../images/ref_point.jpg')
            result = image_processor.show_image(image)
            self.assertEqual(result, 0)
        except Exception:
            self.fail('show_image() raised exception')

    def test_process_image(self):
        self.fail()

    def test_get_ref_point_width(self):
        self.fail()

    def test_get_measurement_px(self):
        self.fail()

    def test_get_measurement_mm(self):
        self.fail()

    def test_get_mm_per_psi(self):
        self.fail()

    def test_calc_ideal_pressure(self):
        self.fail()
