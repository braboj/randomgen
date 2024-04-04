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
        self.bins = ()
        self.probabilities = ()
        self.cumulative_probabilities = []

    def __str__(self):
        return f"Numbers: {self.bins}, Probabilities: {self.probabilities}"

    @abstractmethod
    def set_bins(self, numbers):
        pass

    @abstractmethod
    def validate_bins(self):
        pass

    @abstractmethod
    def set_probabilities(self, probabilities):
        pass

    @abstractmethod
    def validate_probabilities(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def next_num(self):
        pass

    @abstractmethod
    def calc_cdf(self):
        pass

    @abstractmethod
    def generate(self, amount):
        pass


class RandomGenV1(RandomGenABC):


    def set_bins(self, numbers):
        self.bins = numbers
        return self

    def validate_bins(self):

        # Check if the numbers is None
        if self.bins is None:
            raise RandomGenTypeError()

        # Check if the numbers are iterable
        elif not hasattr(self.bins, '__iter__'):
            raise RandomGenTypeError()

        # Check if dictionary
        elif isinstance(self.bins, dict):
            raise RandomGenTypeError()

        # Check if the any member is not a number
        elif not all(isinstance(num, (int, float)) for num in self.bins):
            raise RandomGenTypeError()

        # Check if the numbers list is empty
        elif not self.bins:
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
        elif not all(isinstance(prob, (int, float)) for prob in self.probabilities):
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

        self.validate_bins()
        self.validate_probabilities()

        # Check if the numbers and probabilities' lists have the same length
        if len(self.bins) != len(self.probabilities):
            raise RandomGenMismatchError()

        # After the validation calculate the cumulative probabilities
        self.calc_cdf()

        return self

    def next_num(self):
        rand = random.random()
        for i, cum_prob in enumerate(self.cumulative_probabilities):
            if rand <= cum_prob:
                return self.bins[i]

    def generate(self, amount):
        return [self.next_num() for _ in range(amount)]


class RandomGenV2(RandomGenABC):

    def set_bins(self, numbers):
        self.bins = numbers
        return self

    def validate_bins(self):

        # Check if the numbers is None
        if self.bins is None:
            raise RandomGenTypeError()

        # Check if the numbers are iterable
        elif not hasattr(self.bins, '__iter__'):
            raise RandomGenTypeError()

        # Check if dictionary
        elif isinstance(self.bins, dict):
            raise RandomGenTypeError()

        # Check if the numbers list is not a list of numbers
        elif not all(isinstance(num, (int, float)) for num in self.bins):
            raise RandomGenTypeError()

        # Check if the numbers list is empty
        elif not self.bins:
            raise RandomGenEmptyError()

        return self

    def set_probabilities(self, probabilities):
        self.probabilities = probabilities
        return self

    def validate_probabilities(self):

        # Check if the probabilities is None
        if self.probabilities is None:
            raise RandomGenTypeError()

        # Check if empty
        elif not self.probabilities:
            raise RandomGenEmptyError()

        # Check if the probabilities are iterable
        elif not hasattr(self.probabilities, '__iter__'):
            raise RandomGenTypeError()

        # Check if set
        elif isinstance(self.probabilities, set):
            raise RandomGenTypeError()

        # Check if dictionary
        elif isinstance(self.probabilities, dict):
            raise RandomGenTypeError()

        # Check if the any member is not a number
        elif not all(isinstance(prob, (int, float)) for prob in self.probabilities):
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

        # Validate the numbers and probabilities
        self.validate_bins()
        self.validate_probabilities()

        # Check if the numbers and probabilities' lists have the same length
        if len(self.bins) != len(self.probabilities):
            raise RandomGenMismatchError()

        # After the validation calculate the cumulative probabilities
        self.calc_cdf()

        return self

    def next_num(self):
        # Use random.choices to select a number based on the probabilities
        return random.choices(self.bins, self.probabilities, k=1)[0]

    def generate(self, amount):
        return [self.next_num() for _ in range(amount)]
