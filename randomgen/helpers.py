from collections import Counter


class Histogram(dict):
    """ Helper class to build a histogram from a list of numbers """

    def __init__(self):
        super().__init__()
        self.random_numbers = ()
        self.counter = 0
        self.total = 0

    def set_numbers(self, numbers):
        self.random_numbers = numbers
        return self

    def from_dict(self, histogram):
        self.update(histogram)
        return self

    def calc(self):
        self.counter = Counter(self.random_numbers)
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
        .calc()
    )
    print(h1)

    h2 = Histogram().from_dict(h1)
    print(h2)
