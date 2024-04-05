import random
from collections import Counter
from scipy.stats import chi2
from abc import ABCMeta, abstractmethod

from randomgen.errors import (
    RandomGenTypeError,
    RandomGenEmptyError
)


class HypothesisTestAbc(metaclass=ABCMeta):

    @abstractmethod
    def set_observed_numbers(self, numbers):
        raise NotImplementedError

    @abstractmethod
    def validate_observed_numbers(self):
        raise NotImplementedError

    @abstractmethod
    def set_expected_probabilities(self, probabilities):
        raise NotImplementedError

    @abstractmethod
    def validate_expected_probabilities(self):
        raise NotImplementedError

    @abstractmethod
    def validate(self):
        raise NotImplementedError

    @abstractmethod
    def calc(self, alpha=0.05):
        raise NotImplementedError


class ChiSquareTest(HypothesisTestAbc):

    def __init__(self):
        # Counter for the random numbers
        self.counter = None

        # Total number of random numbers
        self.total = None

        # Histogram of the random numbers
        self.observed = None

        # Expected histogram based on the probabilities
        self.expected = None

        # Chi-square value
        self.chi_square = None

        # Degrees of freedom
        self.df = None

        # P-value
        self.p_value = None

        # Observed random numbers
        self.numbers = ()

        # Given probabilities to test
        self.probabilities = ()

    def __str__(self):
        message = (
            f"Chi-square: {self.chi_square}, "
            f"Degrees of freedom: {self.df}, "
            f"P-value: {self.p_value}",
        )

        return message

    def set_observed_numbers(self, numbers):
        self.numbers = numbers
        return self

    def validate_observed_numbers(self):

        if self.numbers is None:
            raise RandomGenTypeError()

        elif isinstance(self.numbers, dict):
            raise RandomGenTypeError()

        elif not hasattr(self.numbers, '__iter__'):
            raise RandomGenTypeError()

        elif not all(
                isinstance(num, (int, float)) for num in self.numbers):
            raise RandomGenTypeError()

        elif not self.numbers:
            raise RandomGenEmptyError()

        return self

    def set_expected_probabilities(self, probabilities):
        self.probabilities = probabilities
        return self

    def validate_expected_probabilities(self):

        if self.probabilities is None:
            raise RandomGenTypeError()

        elif isinstance(self.probabilities, dict):
            raise RandomGenTypeError()

        elif not hasattr(self.probabilities, '__iter__'):
            raise RandomGenTypeError()

        elif not all(
                isinstance(num, (int, float)) for num in self.probabilities):
            raise RandomGenTypeError()

        elif not self.probabilities:
            raise RandomGenEmptyError()

        return self

    def validate(self):
        self.validate_observed_numbers()
        self.validate_expected_probabilities()
        return self

    def calc(self, alpha=0.05):
        """ Perform the chi-square test for the given significance level

        It tells us how likely it is that the null hypothesis is true. The
        null hypothesis is that the observed distribution is the same as the
        expected distribution.

        Args:
            alpha (float): Significance level

        Returns:
            bool: True if the null hypothesis is not rejected, False otherwise

        """
        # Calculate the frequency of each number
        self.counter = Counter(self.numbers)

        # Calculate the total number of random numbers
        self.total = sum(self.counter.values())

        # Generate the observed histogram
        self.observed = {num: count / self.total for num, count in
                         self.counter.items()}

        # Convert the histogram to a sorted dictionary
        self.observed = dict(sorted(self.observed.items()))

        # Generate the expected histogram based on the probabilities
        # ---------------------------------------------------------
        # This is the expected number of times each number should appear
        # given the probabilities and the total number of random numbers.

        self.expected = {
            num: probability * self.total
            for num, probability
            in zip(self.observed.keys(), self.probabilities)
        }

        # Calculate the chi-square value
        # ------------------------------
        # This is the sum of the squared differences between the observed and
        # expected values divided by the expected values.

        self.chi_square = sum(
            (observed - self.expected[num]) ** 2 / self.expected[num]
            for num, observed
            in self.counter.items()
        )

        # Calculate the degrees of freedom
        # ---------------------------------
        # df = n - k - 1, where n is the number of bins and k is the number of
        # parameters estimated from the data. In this case, k = 0, because the
        # probabilities are given.

        self.df = len(self.counter) - 1

        # Calculate the p-value that corresponds to the chi-square value
        self.p_value = 1 - chi2.cdf(self.chi_square, self.df)

        return self

    def is_null(self, alpha=0.05):

        # Scipy/Numpy hijacks bool somehow, and it becomes a bool_ object.
        # Unfortunately, this causes some problems when comparing the result
        # using the is operator (e.g bool(0.05) is False).

        result = self.p_value > alpha

        return bool(result)


if __name__ == "__main__":
    # Generate random numbers from -1 to 3 in a uniform distribution
    nums = [random.randint(-1, 3) for _ in range(10000)]
    probs = [0.2, 0.2, 0.2, 0.2, 0.2]

    # Create the chi-square test object for a uniform distribution
    # The result should be True
    hypothesis = (
        ChiSquareTest()
        .set_observed_numbers(nums)
        .set_expected_probabilities(probs)
        .calc()
    )

    print("Hypothesis is: ", hypothesis)

    # Now change the probabilities to a different distribution
    # The result should be False
    probs = [0.01, 0.3, 0.58, 0.1, 0.01]

    hypothesis = (
        ChiSquareTest()
        .set_observed_numbers(nums)
        .set_expected_probabilities(probs)
        .calc()
    )

    print("Hypothesis is: ", hypothesis)
