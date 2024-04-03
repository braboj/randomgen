# Calculate the frequency of each number
from collections import Counter
import random


def next_num(numbers, probabilities):
    return random.choices(numbers, probabilities, k=1)[0]


def test():

    # Print the original numbers and their probabilities
    n = [-1, 0, 1, 2, 3]
    p = [0.01, 0.3, 0.58, 0.1, 0.01]
    expected_histogram = dict(zip(n, p))
    expected_histogram = dict(sorted(expected_histogram.items()))
    print(expected_histogram)

    # Generate 1000 random numbers
    random_numbers = [next_num(n, p) for _ in range(10000)]

    # Calculate the frequency and probability of each number
    counter = Counter(random_numbers)
    total = sum(counter.values())
    histogram = {num: count / total for num, count in counter.items()}

    # Sort by key
    histogram = dict(sorted(histogram.items()))
    print(histogram)


if __name__ == "__main__":
    test()
