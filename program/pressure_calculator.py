import numpy as np
import scipy.stats as stats


class PressureCalculator:

    sag = None
    stroke = None
    measurement_100 = None
    measurement_150 = None
    debug = None

    def __init__(self, sag, stroke, debug=False):
        self.sag = sag
        self.stroke = stroke
        self.debug = debug

    def _get_ideal_sag_mm(self):
        ideal = float(self.stroke) * (float(self.sag) / 100.0)
        if self.debug:
            print 'PreCal:_get_ideal_sag_mm:', ideal
        return ideal

    def _get_ideal_pressure(self):
        slope, intercept = self._calculate_linear_equation()
        ideal = (slope * self._get_ideal_sag_mm()) + intercept
        if self.debug:
            print 'PreCal:_get_ideal_pressure:', ideal
        return ideal

    def _calculate_linear_equation(self):
        print self.measurement_100, self.measurement_150
        x = np.array([self.measurement_100, self.measurement_150])
        y = np.array([100, 150])
        slope, intercept, __, __, __ = stats.linregress(x, y)
        if self.debug:
            print 'PreCal:_calculate_linear_equation: {s}x + {i}'.format(s=slope, i=intercept)
        return slope, intercept

    def calculate(self):
        return self._get_ideal_pressure()
