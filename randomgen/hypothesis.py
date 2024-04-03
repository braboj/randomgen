import random
from collections import Counter
from scipy.stats import chi2
from abc import ABCMeta, abstractmethod


class HypothesisTest(metaclass=ABCMeta):

    @abstractmethod
    def test(self, alpha=0.05):
        pass


class ChiSquareTest(HypothesisTest):

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

    def __str__(self):
        message = (
            f"Chi-square: {self.chi_square}, "
            f"Degrees of freedom: {self.df}, "
            f"P-value: {self.p_value}",
        )

        return message

    def set_random_numbers(self, numbers):
        self.random_numbers = numbers
        return self

    def set_probabilities(self, probabilities):
        self.probabilities = probabilities
        return self

    def calc_chi(self):

        # Calculate the frequency of each number
        self.counter = Counter(self.random_numbers)

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

        # Return the object to allow for method chaining
        return self

    def calc_p(self):
        # Calculate the p-value that corresponds to the chi-square value
        self.p_value = 1 - chi2.cdf(self.chi_square, self.df)
        return self

    def test(self, alpha=0.05):
        """ Test the distribution of random numbers against the given

        Probabilities using the chi-square test

        Args:
            alpha (float): Significance level

        Returns:
            bool: True if the null hypothesis is not rejected, False otherwise

        """

        return self.p_value > alpha


if __name__ == "__main__":

    # Generate random numbers from -1 to 3 in a uniform distribution
    nums = [random.randint(-1, 3) for _ in range(1000)]
    probs = [0.2, 0.2, 0.2, 0.2, 0.2]

    # Create the chi-square test object for a uniform distribution
    # The result should be True
    hypothesis = (
        ChiSquareTest()
        .set_random_numbers(nums)
        .set_probabilities(probs)
        .calc_chi()
        .calc_p()
        .test()
    )

    print("Hypothesis is: ", hypothesis)

    # Now change the probabilities to a different distribution
    # The result should be False
    probs = [0.01, 0.3, 0.58, 0.1, 0.01]

    hypothesis = (
        ChiSquareTest()
        .set_random_numbers(nums)
        .set_probabilities(probs)
        .calc_chi()
        .calc_p()
        .test()
    )

    print("Hypothesis is: ", hypothesis)
