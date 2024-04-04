from collections import Counter
from randomgen.errors import (
    RandomGenTypeError,
    RandomGenEmptyError
)


class Histogram(dict):
    """ Helper class to build a histogram from a list of numbers """

    def __init__(self):
        super().__init__()
        self.numbers = ()
        self.counter = 0
        self.total = 0
        self.probabilities = ()

    def from_dict(self, histogram):
        self.update(histogram)
        return self

    def set_numbers(self, numbers):
        self.numbers = numbers
        return self

    def validate_numbers(self):

        # Check if the numbers is None
        if self.numbers is None:
            raise RandomGenTypeError()

        # Check if the numbers are a dictionary
        elif isinstance(self.numbers, dict):
            raise RandomGenTypeError()

        # Check if the numbers are iterable
        elif not hasattr(self.numbers, '__iter__'):
            raise RandomGenTypeError()

        # Check if any member is not a number
        elif not all(isinstance(n, (int, float)) for n in self.numbers):
            raise RandomGenTypeError()

        # Check if the number list is empty
        elif not self.numbers:
            raise RandomGenEmptyError()

        return self

    def validate(self):
        self.validate_numbers()
        return self

    def calc(self):
        self.counter = Counter(self.numbers)
        self.total = sum(self.counter.values())
        self.update(
            {
                num: count / self.total
                for num, count in
                self.counter.items()
            }
        )

        hist = dict(sorted(self.items()))
        self.update(hist)
        return self


if __name__ == "__main__":
    import random

    # Generate 1000 random numbers
    random_numbers = [random.randint(-1, 3) for _ in range(10000)]

    # Create a histogram object
    h1 = (
        Histogram()
        .set_numbers(random_numbers)
        .validate_numbers()
        .calc()
    )
    print(h1)

    h2 = Histogram().from_dict(h1)
    print(h2)
