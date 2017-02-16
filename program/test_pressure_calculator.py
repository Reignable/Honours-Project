from unittest2 import TestCase


class TestPressureCalculator(TestCase):

    pressure_calculator = None

    def setUp(self):
        from pressure_calculator import PressureCalculator
        self.pressure_calculator = PressureCalculator(30, 57, True)

    def tearDown(self):
        pass

    def test_get_ideal_sag_mm_normal(self):
        self.assertIsInstance(self.pressure_calculator._get_ideal_sag_mm(), float)

    def test_get_ideal_pressure(self):
        self.pressure_calculator.measurement_100 = 29
        self.pressure_calculator.measurement_150 = 21
        self.assertIsInstance(self.pressure_calculator._get_ideal_pressure(), float)

    def test_calculate_linear_equation(self):
        self.pressure_calculator.measurement_100 = 29
        self.pressure_calculator.measurement_150 = 21
        self.assertIsInstance(self.pressure_calculator.calculate(), (float, float))
