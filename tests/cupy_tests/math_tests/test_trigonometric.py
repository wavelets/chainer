import unittest

from cupy import testing


@testing.gpu
class TestTrigonometric(unittest.TestCase):

    _multiprocess_can_split_ = True

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(atol=1e-5)
    def check_unary(self, name, xpy, dtype):
        a = testing.shaped_arange((2, 3), xpy, dtype)
        return getattr(xpy, name)(a)

    @testing.for_all_dtypes()
    @testing.numpy_cupy_allclose(atol=1e-5)
    def check_binary(self, name, xpy, dtype):
        a = testing.shaped_arange((2, 3), xpy, dtype)
        b = testing.shaped_reverse_arange((2, 3), xpy, dtype)
        return getattr(xpy, name)(a, b)

    @testing.for_dtypes(['e', 'f', 'd'])
    @testing.numpy_cupy_allclose(atol=1e-5)
    def check_unary_unit(self, name, xpy, dtype):
        a = xpy.array([0.2, 0.4, 0.6, 0.8], dtype=dtype)
        return getattr(xpy, name)(a)

    def test_sin(self):
        self.check_unary('sin')

    def test_cos(self):
        self.check_unary('cos')

    def test_tan(self):
        self.check_unary('tan')

    def test_arcsin(self):
        self.check_unary_unit('arcsin')

    def test_arccos(self):
        self.check_unary_unit('arccos')

    def test_arctan(self):
        self.check_unary('arctan')

    def test_arctan2(self):
        self.check_binary('arctan2')

    def test_hypot(self):
        self.check_binary('hypot')

    def test_deg2rad(self):
        self.check_unary('deg2rad')

    def test_rad2deg(self):
        self.check_unary('rad2deg')