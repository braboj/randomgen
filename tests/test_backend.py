import time

import pytest
from randomgen.core import RandomGenV1, RandomGenV2
from randomgen.hypothesis import ChiSquareTest
from randomgen.errors import *

versions = [RandomGenV1, RandomGenV2]

####################################################################################################
@pytest.fixture(scope="class")
def randomgen(request):
    if hasattr(request, 'param'):
        return request.param()
    return RandomGenV1()  # Default version if none specified

####################################################################################################

@pytest.mark.parametrize("randomgen", versions, indirect=True)
class Test_RG_BINS(object):

    def test_NONE(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_bins(None)
            randomgen.validate()

    def test_EMPTY(self, randomgen):
        with pytest.raises(RandomGenEmptyError):
            randomgen.set_bins([])
            randomgen.validate_bins()

    def test_INT(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_bins(123)
            randomgen.validate_bins()

    def test_INT_LIST(self, randomgen):
        randomgen.set_bins([-1, 0, 1, 2, 3])
        randomgen.validate_bins()
        assert randomgen.bins == [-1, 0, 1, 2, 3]

    def test_INT_TUPLE(self, randomgen):
        randomgen.set_bins((-1, 0, 1, 2, 3))
        randomgen.validate_bins()
        assert randomgen.bins == (-1, 0, 1, 2, 3)

    def test_INT_SET(self, randomgen):
        randomgen.set_bins({-1, 0, 1, 2, 3})
        randomgen.validate_bins()
        assert randomgen.bins == {-1, 0, 1, 2, 3}

    def test_FLOAT(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_bins(123.45)
            randomgen.validate_bins()

    def test_FLOAT_LIST(self, randomgen):
        randomgen.set_bins([-1.0, 0.0, 1.0, 2.0, 3.0])
        randomgen.validate_bins()
        assert randomgen.bins == [-1.0, 0.0, 1.0, 2.0, 3.0]

    def test_FLOAT_TUPLE(self, randomgen):
        randomgen.set_bins((-1.0, 0.0, 1.0, 2.0, 3.0))
        randomgen.validate_bins()
        assert randomgen.bins == (-1.0, 0.0, 1.0, 2.0, 3.0)

    def test_FLOAT_SET(self, randomgen):
        randomgen.set_bins({-1.0, 0.0, 1.0, 2.0, 3.0})
        randomgen.validate_bins()
        assert randomgen.bins == {-1.0, 0.0, 1.0, 2.0, 3.0}

    def test_STRING(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_bins("123")
            randomgen.validate_bins()

    def test_STRING_LIST(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_bins(["-1", "0", "1", "2", "3"])
            randomgen.validate_bins()

    def test_DICT(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_bins({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
            randomgen.validate_bins()

    def test_MIXED_TYPES(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_bins([-1, 0.0, "1", 2.0, 3])
            randomgen.validate_bins()

    def test_MIXED_NUMBERS(self, randomgen):
        randomgen.set_bins([-1, 0, 1, 2.0, 3])
        randomgen.validate_bins()
        assert randomgen.bins == [-1, 0, 1, 2.0, 3]

####################################################################################################

@pytest.mark.parametrize("randomgen", versions, indirect=True)
class Test_RG_PROBABILITIES(object):

    def test_NONE(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities(None)
            randomgen.validate_probabilities()

    def test_EMPTY(self, randomgen):
        with pytest.raises(RandomGenEmptyError):
            randomgen.set_probabilities([])
            randomgen.validate_probabilities()

    def test_INT(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities(123)
            randomgen.validate_probabilities()

    def test_INT_LIST(self, randomgen):
        randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.2])
        randomgen.validate_probabilities()
        assert randomgen.probabilities == [0.2, 0.2, 0.2, 0.2, 0.2]

    def test_INT_TUPLE(self, randomgen):
        randomgen.set_probabilities((0.2, 0.2, 0.2, 0.2, 0.2))
        randomgen.validate_probabilities()
        assert randomgen.probabilities == (0.2, 0.2, 0.2, 0.2, 0.2)

    def test_INT_SET(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities({0.2, 0.2, 0.2, 0.2, 0.2})
            randomgen.validate_probabilities()

    def test_FLOAT(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities(123.45)
            randomgen.validate_probabilities()

    def test_FLOAT_LIST(self, randomgen):
        randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.2])
        randomgen.validate_probabilities()
        assert randomgen.probabilities == [0.2, 0.2, 0.2, 0.2, 0.2]

    def test_FLOAT_TUPLE(self, randomgen):
        randomgen.set_probabilities((0.2, 0.2, 0.2, 0.2, 0.2))
        randomgen.validate_probabilities()
        assert randomgen.probabilities == (0.2, 0.2, 0.2, 0.2, 0.2)

    def test_FLOAT_SET(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities({0.2, 0.2, 0.2, 0.2, 0.2})
            randomgen.validate_probabilities()

    def test_STRING(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities("123")
            randomgen.validate_probabilities()

    def test_STRING_LIST(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities(["-1", "0", "1", "2", "3"])
            randomgen.validate_probabilities()

    def test_DICT(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
            randomgen.validate_probabilities()

    def test_MIXED_TYPES(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities([-1, 0.0, "1", 2.0, 3])
            randomgen.validate_probabilities()

    def test_MIXED_NUMBERS(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities([-0.2, 0.4, 0.2, 0.2, 0.4])
            randomgen.validate_probabilities()

    def test_IS_NEGATIVE(self, randomgen):
        with pytest.raises(RandomGenTypeError):
            randomgen.set_probabilities([0.2, 0.2, 0.2, -0.2, 0.2])
            randomgen.validate_probabilities()

    def test_SIZE_MISMATCH(self, randomgen):
        with pytest.raises(RandomGenMismatchError):
            randomgen.set_bins([1, 2, 3, 4, 5])
            randomgen.set_probabilities([0.1, 0.2, 0.3, 0.4])
            randomgen.validate()

    def test_SUM_IS_ONE(self, randomgen):
        randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.2])
        randomgen.validate_probabilities()
        assert sum(randomgen.probabilities) == 1

    def test_SUM_IS_ZERO(self, randomgen):
        with pytest.raises(RandomGenSumError):
            randomgen.set_probabilities([0.0, 0.0, 0.0, 0.0, 0.0])
            randomgen.validate_probabilities()

    def test_SUM_IS_GREATER_THAN_ONE(self, randomgen):
        with pytest.raises(RandomGenSumError):
            randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.3])
            randomgen.validate()

    def test_SUM_IS_LESS_THAN_ONE(self, randomgen):
        with pytest.raises(RandomGenSumError):
            randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.1])
            randomgen.validate()

####################################################################################################

@pytest.mark.parametrize("randomgen", versions, indirect=True)
class Test_RG_DISTRIBUTION(object):

    def test_FIT_UNIFORM(self, randomgen):

        uniform_probabilities = [0.2, 0.2, 0.2, 0.2, 0.2]

        # Prepare the random generator
        randomgen.set_bins([1, 2, 3, 4, 5])
        randomgen.set_probabilities(uniform_probabilities)
        randomgen.validate()

        # Generate the maximum number of random numbers
        random_numbers = randomgen.generate(amount=1000)

        # Perform the Chi-Square test
        hypothesis = (
            ChiSquareTest()
            .set_numbers(random_numbers)
            .set_probabilities(uniform_probabilities)
            .calculate()
        )

        # Test if the hypothesis is valid
        assert hypothesis.test() == True

    def test_FIT_BINOMIAL(self, randomgen):

        binimoal_probabilities = [0.0625, 0.25, 0.375, 0.25, 0.0625]

        # Prepare the random generator
        randomgen.set_bins([1, 2, 3, 4, 5])
        randomgen.set_probabilities(binimoal_probabilities)
        randomgen.validate()

        # Generate the maximum number of random numbers
        random_numbers = randomgen.generate(amount=1000)

        # Perform the Chi-Square test
        hypothesis = (
            ChiSquareTest()
            .set_numbers(random_numbers)
            .set_probabilities(binimoal_probabilities)
            .calculate()
        )

        # Test if the hypothesis is valid
        assert hypothesis.test() == True


    def test_FIT_CUSTOM(self, randomgen):

        custom_probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

        # Prepare the random generator
        randomgen.set_bins([1, 2, 3, 4, 5])
        randomgen.set_probabilities(custom_probabilities)
        randomgen.validate()

        # Generate the maximum number of random numbers
        random_numbers = randomgen.generate(amount=1000)

        # Perform the Chi-Square test
        hypothesis = (
            ChiSquareTest()
            .set_numbers(random_numbers)
            .set_probabilities(custom_probabilities)
            .calculate()
        )

        # Test if the hypothesis is valid
        assert hypothesis.test() == True


@pytest.mark.parametrize("randomgen", versions, indirect=True)
class Test_RG_PERFORMANCE(object):

    def test_TIME(self, randomgen):

        # Prepare the random generator
        randomgen.set_bins([1, 2, 3, 4, 5])
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