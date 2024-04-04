import random

import pytest

from randomgen.histogram import Histogram
from randomgen.errors import *

versions = [Histogram, ]


# #############################################################################
@pytest.fixture(scope="class")
def histogram(request):
    if hasattr(request, 'param'):
        return request.param()
    return Histogram()  # Default version if none specified


###############################################################################

@pytest.mark.parametrize("histogram", versions, indirect=True)
class TestHistogramParamNumbers(object):

    def test_none(self, histogram):
        with pytest.raises(RandomGenTypeError):
            histogram.set_numbers(None)
            histogram.validate_numbers()

    def test_empty(self, histogram):
        with pytest.raises(RandomGenEmptyError):
            histogram.set_numbers([])
            histogram.validate_numbers()

    def test_int(self, histogram):
        with pytest.raises(RandomGenTypeError):
            histogram.set_numbers(123)
            histogram.validate_numbers()

    def test_int_list(self, histogram):
        histogram.set_numbers([-1, 0, 1, 2, 3])
        histogram.validate_numbers()
        assert histogram.numbers == [-1, 0, 1, 2, 3]

    def test_int_tuple(self, histogram):
        histogram.set_numbers((-1, 0, 1, 2, 3))
        histogram.validate_numbers()
        assert histogram.numbers == (-1, 0, 1, 2, 3)

    def test_int_set(self, histogram):
        histogram.set_numbers({-1, 0, 1, 2, 3})
        histogram.validate_numbers()
        assert histogram.numbers == {-1, 0, 1, 2, 3}

    def test_float(self, histogram):
        with pytest.raises(RandomGenTypeError):
            histogram.set_numbers(123.45)
            histogram.validate_numbers()

    def test_float_list(self, histogram):
        histogram.set_numbers([-1.0, 0.0, 1.0, 2.0, 3.0])
        histogram.validate_numbers()
        assert histogram.numbers == [-1.0, 0.0, 1.0, 2.0, 3.0]

    def test_float_tuple(self, histogram):
        histogram.set_numbers((-1.0, 0.0, 1.0, 2.0, 3.0))
        histogram.validate_numbers()
        assert histogram.numbers == (-1.0, 0.0, 1.0, 2.0, 3.0)

    def test_float_set(self, histogram):
        histogram.set_numbers({-1.0, 0.0, 1.0, 2.0, 3.0})
        histogram.validate_numbers()
        assert histogram.numbers == {-1.0, 0.0, 1.0, 2.0, 3.0}

    def test_string(self, histogram):
        with pytest.raises(RandomGenTypeError):
            histogram.set_numbers("123")
            histogram.validate_numbers()

    def test_string_list(self, histogram):
        with pytest.raises(RandomGenTypeError):
            histogram.set_numbers(["-1", "0", "1", "2", "3"])
            histogram.validate_numbers()

    def test_dict(self, histogram):
        with pytest.raises(RandomGenTypeError):
            histogram.set_numbers({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
            histogram.validate_numbers()

    def test__mixed_types(self, histogram):
        with pytest.raises(RandomGenTypeError):
            histogram.set_numbers([-1, 0.0, "1", 2.0, 3])
            histogram.validate_numbers()

    def test__mixed_numbers(self, histogram):
        histogram.set_numbers([-1, 0, 1, 2.0, 3])
        histogram.validate_numbers()
        assert histogram.numbers == [-1, 0, 1, 2.0, 3]


@pytest.mark.parametrize("histogram", versions, indirect=True)
class TestHistogramFunctional(object):

    def test_from_dict(self, histogram):
        histogram.from_dict({-1: 0.01, 0: 0.3, 1: 0.58, 2: 0.1, 3: 0.01})
        assert list(histogram.keys()) == [-1, 0, 1, 2, 3]
        assert list(histogram.values()) == [0.01, 0.3, 0.58, 0.1, 0.01]

    def test_calc(self, histogram):
        histogram.set_numbers([-1, -1, 0, 0, 1, 1,  2, 2, 3, 3])
        histogram.calc()
        assert list(histogram.keys()) == [-1, 0, 1, 2, 3]
        assert list(histogram.values()) == [0.2, 0.2, 0.2, 0.2, 0.2]


if __name__ == "__main__":
    pytest.main()
