from randomgen.errors import (
    RandomGenMismatchError,
    RandomGenSumError,
    RandomGenEmptyError,
    RandomGenTypeError,
)

import random
from abc import ABCMeta, abstractmethod


class RandomGenABC(metaclass=ABCMeta):

    def __init__(self):
        self.numbers = ()
        self.probabilities = ()
        self.cumulative_probabilities = []

    def __str__(self):
        return f"Numbers: {self.numbers}, Probabilities: {self.probabilities}"

    def from_dict(self, histogram):
        self.numbers = histogram.keys
        self.probabilities = histogram.values
        return self

    def set_numbers(self, numbers):
        self.numbers = numbers
        return self

    def validate_numbers(self):

        # Check if the numbers is None
        if self.numbers is None:
            raise RandomGenTypeError()

        # Check if the numbers are iterable
        elif not hasattr(self.numbers, '__iter__'):
            raise RandomGenTypeError()

        # Check if dictionary
        elif isinstance(self.numbers, dict):
            raise RandomGenTypeError()

        # Check if the any member is not a number
        elif not all(isinstance(num, (int, float)) for num in self.numbers):
            raise RandomGenTypeError()

        # Check if the numbers list is empty
        elif not self.numbers:
            raise RandomGenEmptyError()

        return self

    def set_probabilities(self, probabilities):
        self.probabilities = probabilities
        return self

    def validate_probabilities(self):

        # Check if the probabilities is None
        if self.probabilities is None:
            raise RandomGenTypeError()

        # Check if the numbers are iterable
        elif not hasattr(self.probabilities, '__iter__'):
            raise RandomGenTypeError()

        # Check if empty
        elif not self.probabilities:
            raise RandomGenEmptyError()

        # Check if set
        elif isinstance(self.probabilities, set):
            raise RandomGenTypeError()

        # Check if dictionary
        elif isinstance(self.probabilities, dict):
            raise RandomGenTypeError()

        # Check if the any member is not a number
        elif not all(
                isinstance(prob, (int, float)) for prob in self.probabilities):
            raise RandomGenTypeError()

        # Check if the probabilities are non-negative
        elif any(probability < 0 for probability in self.probabilities):
            raise RandomGenTypeError()

        # Check if the probabilities sum to 1
        elif round(sum(self.probabilities), 3) != 1:
            raise RandomGenSumError()

        return self

    def calc_cdf(self):
        self.cumulative_probabilities = [
            sum(self.probabilities[:i + 1])
            for i in
            range(len(self.probabilities))
        ]

    def validate(self):

        self.validate_numbers()
        self.validate_probabilities()

        # Check if the numbers and probabilities' lists have the same length
        if len(self.numbers) != len(self.probabilities):
            raise RandomGenMismatchError()

        # After the validation calculate the cumulative probabilities
        self.calc_cdf()

        return self

    def generate(self, amount):
        return [self.next_num() for _ in range(amount)]

    @abstractmethod
    def next_num(self):
        pass


class RandomGenV1(RandomGenABC):

    def next_num(self):
        rand = random.random()
        for i, cum_prob in enumerate(self.cumulative_probabilities):
            if rand <= cum_prob:
                return self.numbers[i]


class RandomGenV2(RandomGenABC):

    def next_num(self):
        # Use random.choices to select a number based on the probabilities
        return random.choices(self.numbers, self.probabilities, k=1)[0]


if __name__ == "__main__":

    from randomgen.helpers import Histogram

    rg = (
        RandomGenV1()
        .set_numbers([1, 2, 3])
        .set_probabilities([0.2, 0.2, 0.6])
        .validate()
    )

    random_numbers = rg.generate(10000)

    observed = (
        Histogram()
        .set_numbers(random_numbers)
        .calc()
    )

    # Expected distribution
    expected = dict(zip(rg.numbers, rg.probabilities))
    print("Expected distribution:", expected)

    # Observed distribution
    print("Observed distribution:", observed)