# Histogram Module Reference

## Histogram

Helper class to build a histogram from a list of numbers

Attributes:
- _numbers: A list of numbers.
- _counter: A Counter object to count the occurrences of each number.
- _total: The total number of elements in the list.
- _probabilities: A list of probabilities for each number.

### from_dict()

Set the histogram from a dictionary.

Args:
- histogram: A dictionary of numbers and probabilities.

Returns:
- self: The instance of the class.

### set_numbers()

Set the numbers to build the histogram.

Args:
- numbers: A list of numbers.

Returns:
- self: The instance of the class.

### validate_numbers()

Validate the numbers.

Returns:
- self: The instance of the class.

### validate()

Validate the numbers and probabilities.

Returns:
- self: The instance of the class.

### calc()

Calculate the histogram.

Returns:
- self: The instance of the class.

