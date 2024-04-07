# Core Module Reference

## RandomGenABC

Abstract base class for random number generators.

**Attributes:**
* _numbers: A list of numbers.
* _probabilities: A list of probabilities.
* _cumulative_probabilities: A list of cumulative probabilities.

### from_dict()

Set the numbers and probabilities from a dictionary.

Args:

- dict_obj: A dictionary of numbers and probabilities.

Returns: 

- self: The instance of the class.

### to_dict()

Return the numbers and probabilities as a dictionary.

Returns:

- A dictionary of numbers and respective probabilities.

### set_numbers()

Set the numbers (similar to the categories in a histogram).

Args:

- values: A list of numbers.

Returns:

- self: The instance of the class.

### validate_numbers()

Validate the numbers.

Returns:

- self: The instance of the class.

### set_probabilities()

Set the probabilities.

Args:

- values: A list of probabilities.

Returns:

- self: The instance of the class.

### validate_probabilities()

Validate the probabilities.

Returns:

- self: The instance of the class.

### calc_cdf()

Calculate the cumulative probabilities.

Returns:

- self: The instance of the class.

### validate()

Validate all the attributes of the class.

Returns:

- self: The instance of the class.

### generate()

Generate random numbers based on the probabilities.

Args:

- amount: The number of random numbers to generate.

Returns:

- A list of random numbers.

### next_num()

Abstract method to generate the next random number.

Returns:

- A random number.


## RandomGenV1

Random number generator version 1. Uses the `RandomGenABC` class implements
the `next_num()` method using the random.random() function.

### next_num()

Generate a random number using the random.random() function.

Returns:

- A random number.

## RandomGenV2

Random number generator version 1. Uses the `RandomGenABC` class implements
the `next_num()` method using the random.random() function.

### next_num()

Generate a random number using the random.random() function.

Returns:

- A random number.
