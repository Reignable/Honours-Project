from unittest2 import TestCase


class TestImageProcessor(TestCase):

    image_processor = None
    processed_test_image = None

    def setUp(self):
        from image_processor import ImageProcessor
        self.image_processor = ImageProcessor('test_image.jpg', 30, 150, 57)

    def tearDown(self):
        pass

    def test_show_image_normal(self):
        import cv2
        from image_processor import show_image
        image = cv2.imread('test_image.jpg')
        result = show_image(image, 1)
        self.assertEqual(result, 0)

    def test_show_image_incorrect_path(self):
        import cv2
        from image_processor import show_image
        image = cv2.imread('')
        self.assertRaises(cv2.error, show_image(image, 1))

    def test_process_image_normal(self):
        import cv2
        image = cv2.imread('test_image.jpg')
        gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
        self.processed_test_image = cv2.Canny(blurred, 0, 100, apertureSize=3)
        processed_image = self.image_processor.process_image()
        self.assertEqual(processed_image.all(), self.processed_test_image.all())

    def test_get_ref_point_width_normal(self):
        self.assertIsInstance(self.image_processor.get_ref_point_width(), float)

    def test_get_measurement_px_normal(self):
        import numpy
        self.assertIsInstance(self.image_processor.get_measurement_px(), numpy.int32)

    def test_get_measurement_mm_normal(self):
        measurement_px = self.image_processor.get_measurement_px()
        self.assertIsInstance(self.image_processor.get_measurement_mm(measurement_px), float)

    def test_get_inverse_mm(self):
        measurement_px = self.image_processor.get_measurement_px()
        measurement_mm = self.image_processor.get_measurement_mm(measurement_px)
        self.assertIsInstance(self.image_processor.get_inverse_measurement(measurement_mm), float)

    def test_get_psi_per_mm_normal(self):
        measurement_px = self.image_processor.get_measurement_px()
        measurement_mm = self.image_processor.get_measurement_mm(measurement_px)
        self.assertIsInstance(self.image_processor.get_psi_per_mm(measurement_mm), float)

    def test_calc_ideal_pressure_normal(self):
        measurement_px = self.image_processor.get_measurement_px()
        measurement_mm = self.image_processor.get_measurement_mm(measurement_px)
        inverse_mm = self.image_processor.get_inverse_measurement(measurement_mm)
        mm_per_psi = self.image_processor.get_psi_per_mm(inverse_mm)
        self.assertIsInstance(self.image_processor.calc_ideal_pressure(mm_per_psi), float)
