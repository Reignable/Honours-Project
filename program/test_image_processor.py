from unittest2 import TestCase


class TestImageProcessor(TestCase):

    image_processor = None
    processed_test_image = None

    def setUp(self):
        from image_processor import ImageProcessor
        self.image_processor = ImageProcessor(True)
        self.image_processor.image_path = 'test_image.jpg'

    def tearDown(self):
        pass

    def test_show_image_normal(self):
        import cv2
        from image_processor import show_image
        image = cv2.imread('test_image.jpg')
        result = show_image(image, 1)
        self.assertEqual(result, 0)

    def test_show_image_incorrect_file_path(self):
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
        self.image_processor.image_path = 'test_image.jpg'
        processed_image = self.image_processor._edge_detect()
        self.assertEqual(processed_image.all(), self.processed_test_image.all())

    def test_get_ref_point_width_normal(self):
        self.assertIsInstance(self.image_processor._get_ref_point_width(), float)

    def test_get_ref_point_width_in_range_100(self):
        import warnings
        warnings.filterwarnings('ignore')
        self.image_processor.image_path = '100_psi_ref.jpg'
        manual_result = 384.0
        for i in range(5):
            with self.subTest(i=i):
                result = self.image_processor._get_ref_point_width()
                self.assertTrue(360.0 <= result <= 410.0)

    def test_get_ref_point_width_in_range_150(self):
        import warnings
        warnings.filterwarnings('ignore')
        self.image_processor.image_path = '150_psi_ref.jpg'
        manual_result = 290.0
        for i in range(5):
            with self.subTest(i=i):
                result = self.image_processor._get_ref_point_width()
                self.assertTrue((manual_result*0.9) <= result <= (manual_result*1.1))

    def test_get_ref_point_width_not_none(self):
        self.assertIsNotNone(self.image_processor._get_ref_point_width(), float)

    def test_get_measurement_px_normal(self):
        import numpy
        self.image_processor.edged_image = self.image_processor._edge_detect()
        self.assertIsInstance(self.image_processor._get_measurement_px(), numpy.int32)

    def test_get_measurement_mm_normal(self):
        self.assertIsInstance(self.image_processor.get_measurement('test_image.jpg'), float)
