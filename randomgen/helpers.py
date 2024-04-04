from collections import Counter
import matplotlib.pyplot as plt


class Histogram(object):
    """ Helper class to build a histogram from a list of numbers """

    def __init__(self):
        self.random_numbers = ()
        self.counter = 0
        self.total = 0
        self.histogram = {}

    def __str__(self):
        msg = str(self.histogram)
        return msg

    def set_numbers(self, numbers):
        self.random_numbers = numbers
        return self

    def set_histogram(self, histogram):
        self.histogram = histogram
        return self

    def build(self):
        self.counter = Counter(self.random_numbers)
        self.total = sum(self.counter.values())
        self.histogram = {num: count / self.total for num, count in
                          self.counter.items()}
        self.histogram = dict(sorted(self.histogram.items()))
        return self

    def plot(self):

        # Convert keys to float
        x = [float(k) for k in self.histogram.keys()]
        y = [float(v) for v in self.histogram.values()]
        plt.bar(x, y)
        plt.show()
        return self


if __name__ == "__main__":

    import random

    # Generate 1000 random numbers
    random_numbers = [random.randint(-1, 3) for _ in range(10000)]

    # Create a histogram object
    hist = (
        Histogram()
        .set_numbers(random_numbers)
        .build()
        .plot()
    )
    print(hist)

