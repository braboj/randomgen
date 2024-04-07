# encoding: utf-8
import pytest
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
    """ Test the `observed_numbers` parameter. """

    def test_none(self, hypothesis):
        """ Test the `observed_numbers` parameter with None."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(None)
            hypothesis.validate_observed_numbers()

    def test_empty(self, hypothesis):
        """ Test the `observed_numbers` parameter with an empty list."""

        with pytest.raises(RandomGenEmptyError):
            hypothesis.set_observed_numbers([])
            hypothesis.validate_observed_numbers()

    def test_int(self, hypothesis):
        """ Test the `observed_numbers` parameter with an integer."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(123)
            hypothesis.validate_observed_numbers()

    def test_int_list(self, hypothesis):
        """ Test the `observed_numbers` parameter with an integer list."""

        hypothesis.set_observed_numbers([-1, 0, 1, 2, 3])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1, 0, 1, 2, 3]

    def test_int_tuple(self, hypothesis):
        """ Test the `observed_numbers` parameter with an integer tuple."""

        hypothesis.set_observed_numbers((-1, 0, 1, 2, 3))
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == (-1, 0, 1, 2, 3)

    def test_int_set(self, hypothesis):
        """ Test the `observed_numbers` parameter with an integer set."""

        hypothesis.set_observed_numbers({-1, 0, 1, 2, 3})
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == {-1, 0, 1, 2, 3}

    def test_float(self, hypothesis):
        """ Test the `observed_numbers` parameter with a float."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(123.45)
            hypothesis.validate_observed_numbers()

    def test_float_list(self, hypothesis):
        """ Test the `observed_numbers` parameter with a float list."""

        hypothesis.set_observed_numbers([-1.0, 0.0, 1.0, 2.0, 3.0])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1.0, 0.0, 1.0, 2.0, 3.0]

    def test_float_tuple(self, hypothesis):
        """ Test the `observed_numbers` parameter with a float tuple."""

        hypothesis.set_observed_numbers((-1.0, 0.0, 1.0, 2.0, 3.0))
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == (-1.0, 0.0, 1.0, 2.0, 3.0)

    def test_float_set(self, hypothesis):
        """ Test the `observed_numbers` parameter with a float set."""

        hypothesis.set_observed_numbers({-1.0, 0.0, 1.0, 2.0, 3.0})
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == {-1.0, 0.0, 1.0, 2.0, 3.0}

    def test_string(self, hypothesis):
        """ Test the `observed_numbers` parameter with a string."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers("123")
            hypothesis.validate_observed_numbers()

    def test_string_list(self, hypothesis):
        """ Test the `observed_numbers` parameter with a string list."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(["-1", "0", "1", "2", "3"])
            hypothesis.validate_observed_numbers()

    def test_dict(self, hypothesis):
        """ Test the `observed_numbers` parameter with a dictionary."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
            hypothesis.validate_observed_numbers()

    def test_mixed_types(self, hypothesis):
        """ Test the `observed_numbers` parameter with mixed types."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers([-1, 0.0, "1", 2.0, 3])
            hypothesis.validate_observed_numbers()

    def test_mixed_numbers(self, hypothesis):
        """ Test the `observed_numbers` parameter with mixed numbers."""

        hypothesis.set_observed_numbers([-1, 0, 1, 2.0, 3])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1, 0, 1, 2.0, 3]


##############################################################################

@pytest.mark.parametrize("hypothesis", variations, indirect=True)
class TestChiSquareExpectedParamProbabilities(object):
    """ Test the `expected_probabilities` parameter. """

    def test_none(self, hypothesis):
        """ Test the `expected_probabilities` parameter with None."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(None)
            hypothesis.validate_observed_numbers()

    def test_empty(self, hypothesis):
        """ Test the `expected_probabilities` parameter with an empty list."""

        with pytest.raises(RandomGenEmptyError):
            hypothesis.set_observed_numbers([])
            hypothesis.validate_observed_numbers()

    def test_int(self, hypothesis):
        """ Test the `expected_probabilities` parameter with an integer."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(123)
            hypothesis.validate_observed_numbers()

    def test_int_list(self, hypothesis):
        """ Test the `expected_probabilities` parameter with an integer list."""

        hypothesis.set_observed_numbers([-1, 0, 1, 2, 3])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1, 0, 1, 2, 3]

    def test_int_tuple(self, hypothesis):
        """ Test the `expected_probabilities` parameter with an integer tuple."""

        hypothesis.set_observed_numbers((-1, 0, 1, 2, 3))
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == (-1, 0, 1, 2, 3)

    def test_int_set(self, hypothesis):
        """ Test the `expected_probabilities` parameter with an integer set."""

        hypothesis.set_observed_numbers({-1, 0, 1, 2, 3})
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == {-1, 0, 1, 2, 3}

    def test_float(self, hypothesis):
        """ Test the `expected_probabilities` parameter with a float."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(123.45)
            hypothesis.validate_observed_numbers()

    def test_float_list(self, hypothesis):
        """ Test the `expected_probabilities` parameter with a float list."""

        hypothesis.set_observed_numbers([-1.0, 0.0, 1.0, 2.0, 3.0])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1.0, 0.0, 1.0, 2.0, 3.0]

    def test_float_tuple(self, hypothesis):
        """ Test the `expected_probabilities` parameter with a float tuple."""

        hypothesis.set_observed_numbers((-1.0, 0.0, 1.0, 2.0, 3.0))
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == (-1.0, 0.0, 1.0, 2.0, 3.0)

    def test_float_set(self, hypothesis):
        """ Test the `expected_probabilities` parameter with a float set."""

        hypothesis.set_observed_numbers({-1.0, 0.0, 1.0, 2.0, 3.0})
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == {-1.0, 0.0, 1.0, 2.0, 3.0}

    def test_string(self, hypothesis):
        """ Test the `expected_probabilities` parameter with a string."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers("123")
            hypothesis.validate_observed_numbers()

    def test_string_list(self, hypothesis):
        """ Test the `expected_probabilities` parameter with a string list."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(["-1", "0", "1", "2", "3"])
            hypothesis.validate_observed_numbers()

    def test_dict(self, hypothesis):
        """ Test the `expected_probabilities` parameter with a dictionary."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
            hypothesis.validate_observed_numbers()

    def test_mixed_types(self, hypothesis):
        """ Test the `expected_probabilities` parameter with mixed types."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers([-1, 0.0, "1", 2.0, 3])
            hypothesis.validate_observed_numbers()

    def test_mixed_numbers(self, hypothesis):
        """ Test the `expected_probabilities` parameter with mixed numbers."""

        hypothesis.set_observed_numbers([-1, 0, 1, 2.0, 3])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1, 0, 1, 2.0, 3]


##############################################################################

@pytest.mark.parametrize("hypothesis", variations, indirect=True)
class TestChiSquareFunctional(object):
    """ Test the functional aspects of the ChiSquareTest class. """

    def test_chi_square_pass(self, hypothesis):
        """ Test the ChiSquareTest class with a passing test."""

        (
            hypothesis
            .set_observed_numbers([1, 1, 1, 2, 2, 2])
            .set_expected_probabilities([0.5, 0.5])
            .calc()
        )

        assert hypothesis.is_null() is True

    def test_chi_square_fail(self, hypothesis):
        """ Test the ChiSquareTest class with a failing test."""

        (
            hypothesis
            .set_observed_numbers([1, 1, 1, 2, 2, 2])
            .set_expected_probabilities([0.1, 0.9])
            .calc()
        )

        assert hypothesis.is_null() is False


if __name__ == "__main__":
    pytest.main()
