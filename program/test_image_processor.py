from unittest2 import TestCase


class TestImageProcessor(TestCase):

    image_processor = None
    processed_test_image = None
    TEST_IMAGE_PATH = '100_ref_close.jpg'

    def setUp(self):
        from image_processor import ImageProcessor
        self.image_processor = ImageProcessor(True)
        self.image_processor.image_path = self.TEST_IMAGE_PATH

    def tearDown(self):
        pass

    def test_show_image_normal(self):
        import cv2
        from image_processor import show_image
        image = cv2.imread(self.TEST_IMAGE_PATH)
        result = show_image(image, 1)
        self.assertEqual(result, 0)

    def test_show_image_incorrect_file_path(self):
        import cv2
        from image_processor import show_image
        image = cv2.imread('')
        self.assertRaises(cv2.error, show_image(image, 1))

    def test_process_image_normal(self):
        import cv2
        image = cv2.imread(self.TEST_IMAGE_PATH)
        gray_scaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray_scaled, (5, 5), 0)
        self.processed_test_image = cv2.Canny(blurred, 0, 100, apertureSize=3)
        self.image_processor.image_path = self.TEST_IMAGE_PATH
        processed_image = self.image_processor._edge_detect()
        self.assertEqual(processed_image.all(), self.processed_test_image.all())

    def test_get_ref_point_width_normal(self):
        self.image_processor._find_ref()
        self.assertIsInstance(self.image_processor._get_ref_point_width(), float)

    def test_get_ref_point_width_in_range(self):
        self.image_processor._find_ref()
        width = self.image_processor._get_ref_point_width()
        expected = 565.0
        self.assertTrue((expected*0.9) <= width <= (expected*1.1))

    def test_get_ref_point_width_not_none(self):
        self.image_processor._find_ref()
        self.assertIsNotNone(self.image_processor._get_ref_point_width(), float)

    def test_get_measurement_px_normal(self):
        import numpy
        self.image_processor.edged_image = self.image_processor._edge_detect()
        self.image_processor._find_ref()
        self.assertIsInstance(self.image_processor._get_measurement_px(), numpy.int32)

    def test_get_measurement_px_in_range(self):
        self.image_processor.edged_image = self.image_processor._edge_detect()
        self.image_processor._find_ref()
        measurement = self.image_processor._get_measurement_px()
        expected = 1749
        self.assertTrue((expected * 0.95) <= measurement <= (expected * 1.05))

    def test_get_measurement_mm_normal(self):
        self.assertIsInstance(self.image_processor.get_measurement(self.TEST_IMAGE_PATH), float)

    def test_get_measurement_mm_in_range(self):
        expected = 31.0
        measurement = self.image_processor.get_measurement(self.TEST_IMAGE_PATH)
        self.assertTrue((expected * 0.9) <= measurement <= (expected *1.1))
