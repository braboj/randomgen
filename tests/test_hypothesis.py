import pytest
import random

from randomgen.hypothesis import ChiSquareTest
from randomgen.errors import (
    RandomGenTypeError,
    RandomGenEmptyError
)

variations = [ChiSquareTest, ]


# #############################################################################
@pytest.fixture(scope="class")
def hypothesis(request):
    if hasattr(request, 'param'):
        return request.param()
    return ChiSquareTest()  # Default version if none specified


###############################################################################

@pytest.mark.parametrize("hypothesis", variations, indirect=True)
class TestChiSquareParamObservedNums(object):

    def test_none(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(None)
            hypothesis.validate_observed_numbers()

    def test_empty(self, hypothesis):
        with pytest.raises(RandomGenEmptyError):
            hypothesis.set_observed_numbers([])
            hypothesis.validate_observed_numbers()

    def test_int(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(123)
            hypothesis.validate_observed_numbers()

    def test_int_list(self, hypothesis):
        hypothesis.set_observed_numbers([-1, 0, 1, 2, 3])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1, 0, 1, 2, 3]

    def test_int_tuple(self, hypothesis):
        hypothesis.set_observed_numbers((-1, 0, 1, 2, 3))
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == (-1, 0, 1, 2, 3)

    def test_int_set(self, hypothesis):
        hypothesis.set_observed_numbers({-1, 0, 1, 2, 3})
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == {-1, 0, 1, 2, 3}

    def test_float(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(123.45)
            hypothesis.validate_observed_numbers()

    def test_float_list(self, hypothesis):
        hypothesis.set_observed_numbers([-1.0, 0.0, 1.0, 2.0, 3.0])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1.0, 0.0, 1.0, 2.0, 3.0]

    def test_float_tuple(self, hypothesis):
        hypothesis.set_observed_numbers((-1.0, 0.0, 1.0, 2.0, 3.0))
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == (-1.0, 0.0, 1.0, 2.0, 3.0)

    def test_float_set(self, hypothesis):
        hypothesis.set_observed_numbers({-1.0, 0.0, 1.0, 2.0, 3.0})
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == {-1.0, 0.0, 1.0, 2.0, 3.0}

    def test_string(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers("123")
            hypothesis.validate_observed_numbers()

    def test_string_list(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(["-1", "0", "1", "2", "3"])
            hypothesis.validate_observed_numbers()

    def test_dict(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
            hypothesis.validate_observed_numbers()

    def test_mixed_types(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers([-1, 0.0, "1", 2.0, 3])
            hypothesis.validate_observed_numbers()

    def test_mixed_numbers(self, hypothesis):
        hypothesis.set_observed_numbers([-1, 0, 1, 2.0, 3])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1, 0, 1, 2.0, 3]


##############################################################################

@pytest.mark.parametrize("hypothesis", variations, indirect=True)
class TestChiSquareParamProbabilities(object):

    def test_none(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(None)
            hypothesis.validate_observed_numbers()

    def test_empty(self, hypothesis):
        with pytest.raises(RandomGenEmptyError):
            hypothesis.set_observed_numbers([])
            hypothesis.validate_observed_numbers()

    def test_int(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(123)
            hypothesis.validate_observed_numbers()

    def test_int_list(self, hypothesis):
        hypothesis.set_observed_numbers([-1, 0, 1, 2, 3])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1, 0, 1, 2, 3]

    def test_int_tuple(self, hypothesis):
        hypothesis.set_observed_numbers((-1, 0, 1, 2, 3))
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == (-1, 0, 1, 2, 3)

    def test_int_set(self, hypothesis):
        hypothesis.set_observed_numbers({-1, 0, 1, 2, 3})
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == {-1, 0, 1, 2, 3}

    def test_float(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(123.45)
            hypothesis.validate_observed_numbers()

    def test_float_list(self, hypothesis):
        hypothesis.set_observed_numbers([-1.0, 0.0, 1.0, 2.0, 3.0])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1.0, 0.0, 1.0, 2.0, 3.0]

    def test_float_tuple(self, hypothesis):
        hypothesis.set_observed_numbers((-1.0, 0.0, 1.0, 2.0, 3.0))
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == (-1.0, 0.0, 1.0, 2.0, 3.0)

    def test_float_set(self, hypothesis):
        hypothesis.set_observed_numbers({-1.0, 0.0, 1.0, 2.0, 3.0})
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == {-1.0, 0.0, 1.0, 2.0, 3.0}

    def test_string(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers("123")
            hypothesis.validate_observed_numbers()

    def test_string_list(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(["-1", "0", "1", "2", "3"])
            hypothesis.validate_observed_numbers()

    def test_dict(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
            hypothesis.validate_observed_numbers()

    def test_mixed_types(self, hypothesis):
        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers([-1, 0.0, "1", 2.0, 3])
            hypothesis.validate_observed_numbers()

    def test_mixed_numbers(self, hypothesis):
        hypothesis.set_observed_numbers([-1, 0, 1, 2.0, 3])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1, 0, 1, 2.0, 3]


##############################################################################

@pytest.mark.parametrize("hypothesis", variations, indirect=True)
class TestChiSquareFunctional(object):

    def test_chi_square_pass(self, hypothesis):

        (
            hypothesis
            .set_observed_numbers([1, 1, 1, 2, 2, 2])
            .set_expected_probabilities([0.5, 0.5])
            .calc()
        )

        assert hypothesis.is_null() is True

    def test_chi_square_fail(self, hypothesis):
        (
            hypothesis
            .set_observed_numbers([1, 1, 1, 2, 2, 2])
            .set_expected_probabilities([0.1, 0.9])
            .calc()
        )

        assert hypothesis.is_null() is False


if __name__ == "__main__":
    pytest.main()
