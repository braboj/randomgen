import time
import pytest

from randomgen.core import RandomGenV1, RandomGenV2
from randomgen.hypothesis import ChiSquareTest
from randomgen.errors import *

versions = [RandomGenV1, RandomGenV2]


# #############################################################################
@pytest.fixture(scope="class")
def randomgen(request):
    if hasattr(request, 'param'):
        return request.param()
    return RandomGenV1()  # Default version if none specified


###############################################################################

@pytest.mark.parametrize("randomgen", versions, indirect=True)
class TestRandomGenParamNumbers(object):

    def test_none(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_numbers(None)
            randomgen.validate()

    def test_empty(self, randomgen):
        with pytest.raises(RandomGenEmptyError):
            randomgen.set_numbers([])
            randomgen.validate_numbers()

    def test_int(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_numbers(123)
            randomgen.validate_numbers()

    def test_int_list(self, randomgen):
        randomgen.set_numbers([-1, 0, 1, 2, 3])
        randomgen.validate_numbers()
        assert randomgen.numbers == [-1, 0, 1, 2, 3]

    def test_int_tuple(self, randomgen):
        randomgen.set_numbers((-1, 0, 1, 2, 3))
        randomgen.validate_numbers()
        assert randomgen.numbers == (-1, 0, 1, 2, 3)

    def test_int_set(self, randomgen):
        randomgen.set_numbers({-1, 0, 1, 2, 3})
        randomgen.validate_numbers()
        assert randomgen.numbers == {-1, 0, 1, 2, 3}

    def test_float(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_numbers(123.45)
            randomgen.validate_numbers()

    def test_float_list(self, randomgen):
        randomgen.set_numbers([-1.0, 0.0, 1.0, 2.0, 3.0])
        randomgen.validate_numbers()
        assert randomgen.numbers == [-1.0, 0.0, 1.0, 2.0, 3.0]

    def test_float_tuple(self, randomgen):
        randomgen.set_numbers((-1.0, 0.0, 1.0, 2.0, 3.0))
        randomgen.validate_numbers()
        assert randomgen.numbers == (-1.0, 0.0, 1.0, 2.0, 3.0)

    def test_float_set(self, randomgen):
        randomgen.set_numbers({-1.0, 0.0, 1.0, 2.0, 3.0})
        randomgen.validate_numbers()
        assert randomgen.numbers == {-1.0, 0.0, 1.0, 2.0, 3.0}

    def test_string(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_numbers("123")
            randomgen.validate_numbers()

    def test_string_list(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_numbers(["-1", "0", "1", "2", "3"])
            randomgen.validate_numbers()

    def test_dict(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_numbers({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
            randomgen.validate_numbers()

    def test__mixed_types(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_numbers([-1, 0.0, "1", 2.0, 3])
            randomgen.validate_numbers()

    def test__mixed_numbers(self, randomgen):
        randomgen.set_numbers([-1, 0, 1, 2.0, 3])
        randomgen.validate_numbers()
        assert randomgen.numbers == [-1, 0, 1, 2.0, 3]


###############################################################################

@pytest.mark.parametrize("randomgen", versions, indirect=True)
class TestRandomGenParamProbabilities(object):

    def test_none(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities(None)
            randomgen.validate_probabilities()

    def test_empty(self, randomgen):
        with pytest.raises(RandomGenEmptyError):
            randomgen.set_probabilities([])
            randomgen.validate_probabilities()

    def test_int(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities(123)
            randomgen.validate_probabilities()

    def test_int_list(self, randomgen):
        randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.2])
        randomgen.validate_probabilities()
        assert randomgen.probabilities == [0.2, 0.2, 0.2, 0.2, 0.2]

    def test_int_tuple(self, randomgen):
        randomgen.set_probabilities((0.2, 0.2, 0.2, 0.2, 0.2))
        randomgen.validate_probabilities()
        assert randomgen.probabilities == (0.2, 0.2, 0.2, 0.2, 0.2)

    def test_int_set(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities({0.2, 0.2, 0.2, 0.2, 0.2})
            randomgen.validate_probabilities()

    def test_float(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities(123.45)
            randomgen.validate_probabilities()

    def test_float_list(self, randomgen):
        randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.2])
        randomgen.validate_probabilities()
        assert randomgen.probabilities == [0.2, 0.2, 0.2, 0.2, 0.2]

    def test_float_tuple(self, randomgen):
        randomgen.set_probabilities((0.2, 0.2, 0.2, 0.2, 0.2))
        randomgen.validate_probabilities()
        assert randomgen.probabilities == (0.2, 0.2, 0.2, 0.2, 0.2)

    def test_float_set(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities({0.2, 0.2, 0.2, 0.2, 0.2})
            randomgen.validate_probabilities()

    def test_string(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities("123")
            randomgen.validate_probabilities()

    def test_string_list(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities(["-1", "0", "1", "2", "3"])
            randomgen.validate_probabilities()

    def test_dict(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
            randomgen.validate_probabilities()

    def test__mixed_types(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities([-1, 0.0, "1", 2.0, 3])
            randomgen.validate_probabilities()

    def test__mixed_numbers(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities([-0.2, 0.4, 0.2, 0.2, 0.4])
            randomgen.validate_probabilities()

    def test__is_negative(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities([0.2, 0.2, 0.2, -0.2, 0.2])
            randomgen.validate_probabilities()

    def test_size_mismatch(self, randomgen):
        with pytest.raises(RandomGenMismatchError):
            randomgen.set_numbers([1, 2, 3, 4, 5])
            randomgen.set_probabilities([0.1, 0.2, 0.3, 0.4])
            randomgen.validate()

    def test_sum_is_one(self, randomgen):
        randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.2])
        randomgen.validate_probabilities()
        assert sum(randomgen.probabilities) == 1

    def test_sum_is_zero(self, randomgen):
        with pytest.raises(RandomGenSumError):
            randomgen.set_probabilities([0.0, 0.0, 0.0, 0.0, 0.0])
            randomgen.validate_probabilities()

    def test_sum_is_greater_than_one(self, randomgen):
        with pytest.raises(RandomGenSumError):
            randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.3])
            randomgen.validate()

    def test_sum_is_less_than_one(self, randomgen):
        with pytest.raises(RandomGenSumError):
            randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.1])
            randomgen.validate()


###############################################################################

@pytest.mark.parametrize("randomgen", versions, indirect=True)
class TestRandomGenDistribution(object):

    def test_fit_uniform(self, randomgen):
        uniform_probabilities = [0.2, 0.2, 0.2, 0.2, 0.2]

        # Prepare the random generator
        randomgen.set_numbers([1, 2, 3, 4, 5])
        randomgen.set_probabilities(uniform_probabilities)
        randomgen.validate()

        # Generate the maximum number of random numbers
        random_numbers = [randomgen.next_num() for _ in range(1000)]

        # Perform the Chi-Square test
        hypothesis = (
            ChiSquareTest()
            .set_observed_numbers(random_numbers)
            .set_expected_probabilities(uniform_probabilities)
        )

        # Test if the hypothesis is valid
        assert  hypothesis.test() is True

    def test_fit_binomial(self, randomgen):
        binomial_probabilities = [0.0625, 0.25, 0.375, 0.25, 0.0625]

        # Prepare the random generator
        randomgen.set_numbers([1, 2, 3, 4, 5])
        randomgen.set_probabilities(binomial_probabilities)
        randomgen.validate()

        # Generate the maximum number of random numbers
        random_numbers = [randomgen.next_num() for _ in range(1000)]

        # Perform the Chi-Square test
        hypothesis = (
            ChiSquareTest()
            .set_observed_numbers(random_numbers)
            .set_expected_probabilities(binomial_probabilities)
        )

        # Test if the hypothesis is valid
        assert hypothesis.test() is True

    def test_fit_custom(self, randomgen):
        custom_probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

        # Prepare the random generator
        randomgen.set_numbers([1, 2, 3, 4, 5])
        randomgen.set_probabilities(custom_probabilities)
        randomgen.validate()

        # Generate the maximum number of random numbers
        random_numbers = [randomgen.next_num() for _ in range(1000)]

        # Perform the Chi-Square test
        hypothesis = (
            ChiSquareTest()
            .set_observed_numbers(random_numbers)
            .set_expected_probabilities(custom_probabilities)
        )

        # Test if the hypothesis is valid
        assert hypothesis.test() is True


@pytest.mark.parametrize("randomgen", versions, indirect=True)
class TestRandomGenPerformance(object):

    def test_time(self, randomgen):
        # Prepare the random generator
        randomgen.set_numbers([1, 2, 3, 4, 5])
        randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.2])
        randomgen.validate()

        # Start measuring the time
        timestamp_1 = time.time_ns()

        # Generate the maximum number of random numbers
        randomgen.generate(amount=1000)

        # Stop measuring the time
        timestamp_2 = time.time_ns()

        # Test if the time is less than 25 msec
        delta = timestamp_2 - timestamp_1
        assert delta < 50e7


if __name__ == "__main__":
    pytest.main()
