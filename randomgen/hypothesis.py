# encoding: utf-8

import random
from scipy.stats import chi2
from collections import Counter
from abc import ABCMeta, abstractmethod

from randomgen.errors import (
    RandomGenTypeError,
    RandomGenEmptyError
)


class HypothesisTestAbc(metaclass=ABCMeta):

    @abstractmethod
    def set_observed_numbers(self, values):
        raise NotImplementedError

    @abstractmethod
    def validate_observed_numbers(self):
        raise NotImplementedError

    @abstractmethod
    def set_expected_probabilities(self, values):
        raise NotImplementedError

    @abstractmethod
    def validate_expected_probabilities(self):
        raise NotImplementedError

    @abstractmethod
    def validate(self):
        raise NotImplementedError

    @abstractmethod
    def calc(self):
        raise NotImplementedError

    @abstractmethod
    def is_null(self, alpha=0.05):
        raise NotImplementedError


class ChiSquareTest(HypothesisTestAbc):

    def __init__(self):
        # Counter for the random numbers
        self._counter = None

        # Total number of random numbers
        self._total = None

        # Histogram of the random numbers
        self._observed = None

        # Expected histogram based on the probabilities
        self._expected = None

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
        message = (f"Chi-square: {self.chi_square} df: {self.df} P-value"
                   f":{self.p_value} Null hypothesis: {self.is_null()}")

        return message

    def set_observed_numbers(self, values):
        self.numbers = values
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

    def set_expected_probabilities(self, values):
        self.probabilities = values
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

    def calc(self):
        """ Perform the chi-square test for the given significance level

        It tells us how likely it is that the null hypothesis is true. The
        null hypothesis is that the observed distribution is the same as the
        expected distribution.

        """

        # Calculate the frequency of each number
        self._counter = Counter(self.numbers)

        # Calculate the total number of random numbers
        self._total = sum(self._counter.values())

        # Generate the observed histogram
        self._observed = {num: count / self._total for num, count in
                          self._counter.items()}

        # Convert the histogram to a sorted dictionary
        self._observed = dict(sorted(self._observed.items()))

        # Generate the expected histogram based on the probabilities
        # ---------------------------------------------------------
        # This is the expected number of times each number should appear
        # given the probabilities and the total number of random numbers.

        self._expected = {
            num: probability * self._total
            for num, probability
            in zip(self._observed.keys(), self.probabilities)
        }

        # Calculate the chi-square value
        # ------------------------------
        # This is the sum of the squared differences between the observed and
        # expected values divided by the expected values.

        self.chi_square = sum(
            (observed - self._expected[num]) ** 2 / self._expected[num]
            for num, observed
            in self._counter.items()
        )

        # Calculate the degrees of freedom
        # ---------------------------------
        # df = n - k - 1, where n is the number of bins and k is the number of
        # parameters estimated from the data. In this case, k = 0, because the
        # probabilities are given.

        self.df = len(self._counter) - 1

        # Calculate the p-value that corresponds to the chi-square value
        self.p_value = 1 - chi2.cdf(self.chi_square, self.df)

        return self

    def is_null(self, alpha=0.05):

        # Scipy/Numpy hijacks bool somehow, and it becomes a bool_ object.
        # Unfortunately, this causes some problems when comparing the result
        # using the is operator (e.g bool(0.05) is False).

        return bool(self.p_value > alpha)


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

    print("Hypothesis is: ", hypothesis.is_null())

    # Now change the probabilities to a different distribution
    # The result should be False
    probs = [0.01, 0.3, 0.58, 0.1, 0.01]

    hypothesis = (
        ChiSquareTest()
        .set_observed_numbers(nums)
        .set_expected_probabilities(probs)
        .calc()
    )

    print("Hypothesis is: ", hypothesis.is_null())
