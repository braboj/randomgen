from randomgen.core import RandomGenV1, RandomGenV2
from randomgen.helpers import Histogram
from randomgen.hypothesis import ChiSquareTest


def main(randomgen):
    """ Random generator application

    Args:
        randomgen (RandomGenABC): Random generator class to use

    """

    print(f"Using random generator: {randomgen.__name__}")

    # Data to test the random generator
    n = 10000
    nums = (-1, 0, 1, 2, 3)
    prob = (0.01, 0.3, 0.58, 0.1, 0.01)
    # prob = (0.2, 0.2, 0.2, 0.2, 0.2)

    # Example usage using a fluent interface
    rg = (
        randomgen()
        .set_bins(nums)
        .set_probabilities(prob)
        .validate()
    )

    # Generate N random numbers
    randoms = [rg.next_num() for _ in range(n)]

    # Print the expected histogram and the actual histogram
    expected = (
        Histogram()
        .set_histogram(dict(zip(nums, prob)))
        # .plot()
    )
    print(f"Expected histogram: {expected}")

    # Calculate the frequency and probability of each number
    observed = (
        Histogram()
        .set_numbers(randoms)
        .build()
        # .plot()
    )
    print(f"Observed histogram: {observed}")

    # Test the distribution of random numbers
    hypothesis = (
        ChiSquareTest()
        .set_numbers(randoms)
        .set_probabilities(prob)
        .calculate()
        .test()
    )
    print("Hypothesis is: ", hypothesis)


if __name__ == "__main__":
    main(RandomGenV1)
    main(RandomGenV2)
