from randomgen.errors import (
    RandomGenLengthError,
    RandomGenSumError,
    RandomGenNegativeError
)

import random
from abc import ABCMeta, abstractmethod


class RandomGenABC(metaclass=ABCMeta):

    def __init__(self):
        self.numbers = ()
        self.probabilities = ()

    def __str__(self):
        return f"Numbers: {self.numbers}, Probabilities: {self.probabilities}"

    @abstractmethod
    def set_numbers(self, numbers):
        pass

    @abstractmethod
    def set_probabilities(self, probabilities):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def next_num(self):
        pass


class RandomGenV1(RandomGenABC):

    def __init__(self):
        super().__init__()
        self.cumulative_probabilities = []

    def set_numbers(self, numbers):
        self.numbers = numbers
        return self

    def set_probabilities(self, probabilities):
        self.probabilities = probabilities
        self.cumulative_probabilities = [sum(probabilities[:i + 1]) for i in
                                         range(len(probabilities))]
        return self

    def validate(self):

        # Check if the numbers and probabilities' lists have the same length
        if len(self.numbers) != len(self.probabilities):
            raise RandomGenLengthError()

        # Check if the probabilities sum to 1
        if sum(self.probabilities) != 1:
            raise RandomGenSumError()

        # Check if the probabilities are non-negative
        if any(probability < 0 for probability in self.probabilities):
            raise RandomGenNegativeError()

        return self

    def next_num(self):
        rand = random.random()
        for i, cum_prob in enumerate(self.cumulative_probabilities):
            if rand <= cum_prob:
                return self.numbers[i]


class RandomGenV2(RandomGenABC):

    def set_numbers(self, numbers):
        self.numbers = numbers
        return self

    def set_probabilities(self, probabilities):
        self.probabilities = probabilities
        return self

    def validate(self):

        # Check if the numbers and probabilities' lists have the same length
        if len(self.numbers) != len(self.probabilities):
            raise RandomGenLengthError()

        # Check if the probabilities sum to 1
        if sum(self.probabilities) != 1:
            raise RandomGenSumError()

        # Check if the probabilities are non-negative
        if any(probability < 0 for probability in self.probabilities):
            raise RandomGenNegativeError()

        return self

    def next_num(self):
        # Use random.choices to select a number based on the probabilities
        return random.choices(self.numbers, self.probabilities, k=1)[0]
