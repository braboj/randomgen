# Errors Module Full Documentation

## HypothesisTestAbc

Abstract base class for hypothesis tests. 

### set_observed_numbers()

Set the observed random numbers.

Args:
- values: A list of random numbers.

Returns:
- self: The instance of the class.

### validate_observed_numbers()

Validate the observed random numbers.

Returns:
- self: The instance of the class.

### set_expected_probabilities()

Set the expected probabilities.

Args:
- values: A list of probabilities.

Returns:
- self: The instance of the class.

### validate_expected_probabilities()

Validate the expected probabilities.

Returns:
- self: The instance of the class.

### validate()

Validate the observed random numbers and expected probabilities.

Returns:
- self: The instance of the class.

### calc()

Perform the hypothesis test.

Returns:
- self: The instance of the class.

### is_null()

Check if the null hypothesis is true.

Args:
- alpha: The significance level.

Returns:
- bool: True if the null hypothesis is true, False otherwise.

## ChiSquareTest

Perform the chi-square test for a given significance level.

The Chi-square test is used to determine if there is a significant
difference between the expected and observed frequencies of random
numbers. It is used to test the null hypothesis that the observed
distribution is the same as the expected distribution.

Attributes:
- _counter: A Counter object to count the occurrences of each number.
- _total: The total number of elements in the list.
- _observed: A histogram of the observed random numbers.
- _expected: A histogram of the expected random numbers.
- chi_square: The chi-square value.
- df: The degrees of freedom.
- p_value: The p-value.
- numbers: The observed random numbers.
- probabilities: The expected probabilities.

### __init__()

No description available.

### __str__()

No description available.

### set_observed_numbers()

Set the observed random numbers.

Args:
- values: A list of random numbers.

Returns:
- self: The instance of the class.

### validate_observed_numbers()

Validate the observed random numbers.

Returns:
- self: The instance of the class.

### set_expected_probabilities()

Set the expected probabilities.

Args:
- values: A list of probabilities.

Returns:
- self: The instance of the class.

### validate_expected_probabilities()

Validate the expected probabilities.

Returns:
- self: The instance of the class.

### validate()

Validate the observed random numbers and expected probabilities.

Returns:
- self: The instance of the class.

### calc()

Perform the chi-square test for the given significance level

It tells us how likely it is that the null hypothesis is true. The
null hypothesis is that the observed distribution is the same as the
expected distribution.

Returns:
- self: The instance of the class.

### is_null()

Check if the null hypothesis is true.

Args:
- alpha: The significance level.

Returns:
- bool: True if the null hypothesis is true, False otherwise.

Notes:
- Scipy/Numpy hijacks bool somehow, and it becomes a bool_ object.
- Unfortunately, this causes some problems when comparing the
- result using the is operator (e.g bool(0.05) is False).

