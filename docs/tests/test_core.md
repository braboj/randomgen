# Core Module Tests

## TestRandomGenParamNumbers
**Description**: Test the `numbers` parameter.


### test_none
- **Description**: Test the `numbers` parameter with None.
- **Code Snippet**:

```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_numbers(None)
    randomgen.validate()
```

### test_empty

- **Description**: Test the `numbers` parameter with an empty list.
- **Code Snippet**:
```text
with pytest.raises(RandomGenEmptyError):
    randomgen.set_numbers([])
    randomgen.validate_numbers()
```

### test_int

- **Description**: Test the `numbers` parameter with an integer.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_numbers(123)
    randomgen.validate_numbers()
```

### test_int_list

- **Description**: Test the `numbers` parameter with an integer list.
- **Code Snippet**:
```text
randomgen.set_numbers([-1, 0, 1, 2, 3])
randomgen.validate_numbers()
assert randomgen._numbers == [-1, 0, 1, 2, 3]
```

### test_int_tuple

- **Description**: Test the `numbers` parameter with an integer tuple.
- **Code Snippet**:
```text
randomgen.set_numbers((-1, 0, 1, 2, 3))
randomgen.validate_numbers()
assert randomgen._numbers == (-1, 0, 1, 2, 3)
```

### test_int_set

- **Description**: Test the `numbers` parameter with an integer set.
- **Code Snippet**:
```text
randomgen.set_numbers({-1, 0, 1, 2, 3})
randomgen.validate_numbers()
assert randomgen._numbers == {-1, 0, 1, 2, 3}
```

### test_float

- **Description**: Test the `numbers` parameter with a float.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_numbers(123.45)
    randomgen.validate_numbers()
```

### test_float_list

- **Description**: Test the `numbers` parameter with a float list.
- **Code Snippet**:
```text
randomgen.set_numbers([-1.0, 0.0, 1.0, 2.0, 3.0])
randomgen.validate_numbers()
assert randomgen._numbers == [-1.0, 0.0, 1.0, 2.0, 3.0]
```

### test_float_tuple

- **Description**: Test the `numbers` parameter with a float tuple.
- **Code Snippet**:
```text
randomgen.set_numbers((-1.0, 0.0, 1.0, 2.0, 3.0))
randomgen.validate_numbers()
assert randomgen._numbers == (-1.0, 0.0, 1.0, 2.0, 3.0)
```

### test_float_set

- **Description**: Test the `numbers` parameter with a float set.
- **Code Snippet**:
```text
randomgen.set_numbers({-1.0, 0.0, 1.0, 2.0, 3.0})
randomgen.validate_numbers()
assert randomgen._numbers == {-1.0, 0.0, 1.0, 2.0, 3.0}
```

### test_string

- **Description**: Test the `numbers` parameter with a string.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_numbers("123")
    randomgen.validate_numbers()
```

### test_string_list

- **Description**: Test the `numbers` parameter with a string list.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_numbers(["-1", "0", "1", "2", "3"])
    randomgen.validate_numbers()
```

### test_dict

- **Description**: Test the `numbers` parameter with a dictionary.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_numbers({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
    randomgen.validate_numbers()
```

### test_mixed_types

- **Description**: Test the `numbers` parameter with mixed types.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_numbers([-1, 0.0, "1", 2.0, 3])
    randomgen.validate_numbers()
```

### test_mixed_numbers`

- **Description**: Test the `numbers` parameter with mixed numbers.
- **Code Snippet**:
```text
randomgen.set_numbers([-1, 0, 1, 2.0, 3])
randomgen.validate_numbers()
assert randomgen._numbers == [-1, 0, 1, 2.0, 3]

```


## TestRandomGenParamProbabilities
**Description**: Test the `probabilities` parameter.


### test_none
- **Description**: Test the `probabilities` parameter with None.
- **Code Snippet**:

```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_probabilities(None)
    randomgen.validate()

```

### test_empty

- **Description**: Test the `probabilities` parameter with an empty list.
- **Code Snippet**:
```text
with pytest.raises(RandomGenEmptyError):
    randomgen.set_probabilities([])
    randomgen.validate_numbers()
```

### test_int

- **Description**: Test the `probabilities` parameter with an integer.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_probabilities(123)
    randomgen.validate_numbers()
```

### test_int_list

- **Description**: Test the `probabilities` parameter with an integer list.
- **Code Snippet**:
```text
randomgen.set_probabilities([-1, 0, 1, 2, 3])
randomgen.validate_numbers()
assert randomgen._numbers == [-1, 0, 1, 2, 3]
```

### test_int_tuple

- **Description**: Test the `probabilities` parameter with an integer tuple.
- **Code Snippet**:
```text
randomgen.set_probabilities((-1, 0, 1, 2, 3))
randomgen.validate_numbers()
assert randomgen._numbers == (-1, 0, 1, 2, 3)
```

### test_int_set

- **Description**: Test the `probabilities` parameter with an integer set.
- **Code Snippet**:
```text
randomgen.set_probabilities({-1, 0, 1, 2, 3})
randomgen.validate_numbers()
assert randomgen._numbers == {-1, 0, 1, 2, 3}
```

### test_float

- **Description**: Test the `probabilities` parameter with a float.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_probabilities(123.45)
    randomgen.validate_numbers()
```

### test_float_list

- **Description**: Test the `probabilities` parameter with a float list.
- **Code Snippet**:
```text
randomgen.set_probabilities([-1.0, 0.0, 1.0, 2.0, 3.0])
randomgen.validate_numbers()
assert randomgen._numbers == [-1.0, 0.0, 1.0, 2.0, 3.0]
```

### test_float_tuple

- **Description**: Test the `probabilities` parameter with a float tuple.
- **Code Snippet**:
```text
randomgen.set_probabilities((-1.0, 0.0, 1.0, 2.0, 3.0))
randomgen.validate_numbers()
assert randomgen._numbers == (-1.0, 0.0, 1.0, 2.0, 3.0)
```

### test_float_set

- **Description**: Test the `probabilities` parameter with a float set.
- **Code Snippet**:
```text
randomgen.set_probabilities({-1.0, 0.0, 1.0, 2.0, 3.0})
randomgen.validate_numbers()
assert randomgen._numbers == {-1.0, 0.0, 1.0, 2.0, 3.0}
```

### test_string

- **Description**: Test the `probabilities` parameter with a string.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_probabilities("123")
    randomgen.validate_numbers()
```

### test_string_list

- **Description**: Test the `probabilities` parameter with a string list.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_probabilities(["-1", "0", "1", "2", "3"])
    randomgen.validate_numbers()
```

### test_dict

- **Description**: Test the `probabilities` parameter with a dictionary.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_probabilities({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
    randomgen.validate_numbers()
```

### test_mixed_types

- **Description**: Test the `probabilities` parameter with mixed types.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_probabilities([-1, 0.0, "1", 2.0, 3])
    randomgen.validate_numbers()
```

### test_mixed_numbers

- **Description**: Test the `probabilities` parameter with mixed numbers.
- **Code Snippet**:
```text
randomgen.set_probabilities([-1, 0, 1, 2.0, 3])
randomgen.validate_numbers()
assert randomgen._numbers == [-1, 0, 1, 2.0, 3]

```

### test_is_negative

- **Description**: Test the `probabilities` parameter with negative numbers.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    randomgen.set_probabilities([0.2, 0.2, 0.2, -0.2, 0.2])
    randomgen.validate_probabilities()
```

### test_size_mismatch

- **Description**: Test the `probabilities` parameter with a size mismatch.
- **Code Snippet**:
```text
with pytest.raises(RandomGenMismatchError):
    randomgen.set_numbers([1, 2, 3, 4, 5])
    randomgen.set_probabilities([0.1, 0.2, 0.3, 0.4])
    randomgen.validate()
```

### test_sum_is_one

- **Description**: Test the `probabilities` parameter with a sum of one.
- **Code Snippet**:
```text
randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.2])
randomgen.validate_probabilities()
assert sum(randomgen._probabilities) == 1
```

### test_sum_is_zero

- **Description**: Test the `probabilities` parameter with a sum of zero.
- **Code Snippet**:
```text
with pytest.raises(RandomGenProbabilitySumError):
    randomgen.set_probabilities([0.0, 0.0, 0.0, 0.0, 0.0])
    randomgen.validate_probabilities()
```

### sum_is_greater_than_one

- **Description**: Test the `probabilities` parameter with a sum of zero.
- **Code Snippet**:
```text
with pytest.raises(RandomGenProbabilitySumError):
    randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.3])
    randomgen.validate()
```

### test_sum_is_less_than_one

- **Description**: Test the `probabilities` parameter with a sum of zero.
- **Code Snippet**:
```text
with pytest.raises(RandomGenProbabilitySumError):
    randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.1])
    randomgen.validate()
```

## TestRandomGenDistribution
**Description**: Test the distribution quality of random numbers.


### test_fit_pass
- **Description**: Test that the distribution fits on big sample size.
- **Code Snippet**:

```text
custom_probabilities = [0.5, 0.5]

# Prepare the random generator
randomgen.set_numbers([1, 2])
randomgen.set_probabilities(custom_probabilities)
randomgen.validate()

# Generate the maximum number of random numbers
random_numbers = [1] * 200 + [2] * 200

# Perform the Chi-Square test
hypothesis = (
    ChiSquareTest()
    .set_observed_numbers(random_numbers)
    .set_expected_probabilities(custom_probabilities)
    .calc()
)

# Test if the hypothesis is valid
assert hypothesis.is_null() is True
```

### test_fit_pass
- **Description**: Test that the distribution fails on small sample size.
- **Code Snippet**:

```text
custom_probabilities = [0.5, 0.5]

# Prepare the random generator
randomgen.set_numbers([1, 2])
randomgen.set_probabilities(custom_probabilities)
randomgen.validate()

# Generate the maximum number of random numbers
random_numbers = [1] * 10 + [2] * 100

# Perform the Chi-Square test
hypothesis = (
    ChiSquareTest()
    .set_observed_numbers(random_numbers)
    .set_expected_probabilities(custom_probabilities)
    .calc()
)

# Test if the hypothesis is valid
assert hypothesis.is_null() is False
```

## TestRandomGenPerformance
**Description**: Test the performance of the random generator.


### test_time
- **Description**: Test that the time execution is below 50ms
- **Code Snippet**:
```text
# Prepare the random generator
randomgen.set_numbers([1, 2, 3, 4, 5])
randomgen.set_probabilities([0.2, 0.2, 0.2, 0.2, 0.2])
randomgen.validate()

# Start measuring the time
timestamp_1 = time.time_ns()

# Generate the maximum number of random numbers
randomgen.generate(amount=1000)

# Stop measuring the time
timestamp_2 = time.time_ns()

# Test if the time is less than 25 msec
delta = timestamp_2 - timestamp_1
assert delta < 50e7
```