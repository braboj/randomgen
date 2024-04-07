# Hypothesis Module Tests

## TestChiSquareParamObservedNums
**Description**: Test the `observed_numbers` parameter.


### test_none

- **Description**: Test the `observed_numbers` parameter with None.
- **Code Snippet**:
```
def test_none(self, hypothesis):
        """ Test the `observed_numbers` parameter with None."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(None)
            hypothesis.validate_observed_numbers()
```

### test_empty

- **Description**: Test the `observed_numbers` parameter with an empty list.
- **Code Snippet**:
```
def test_empty(self, hypothesis):
        """ Test the `observed_numbers` parameter with an empty list."""

        with pytest.raises(RandomGenEmptyError):
            hypothesis.set_observed_numbers([])
            hypothesis.validate_observed_numbers()
```

### test_int

- **Description**: Test the `observed_numbers` parameter with an integer.
- **Code Snippet**:
```
def test_int(self, hypothesis):
        """ Test the `observed_numbers` parameter with an integer."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(123)
            hypothesis.validate_observed_numbers()
```

### test_int_list

- **Description**: Test the `observed_numbers` parameter with an integer list.
- **Code Snippet**:
```
def test_int_list(self, hypothesis):
        """ Test the `observed_numbers` parameter with an integer list."""

        hypothesis.set_observed_numbers([-1, 0, 1, 2, 3])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1, 0, 1, 2, 3]
```

### test_int_tuple

- **Description**: Test the `observed_numbers` parameter with an integer tuple.
- **Code Snippet**:
```
def test_int_tuple(self, hypothesis):
        """ Test the `observed_numbers` parameter with an integer tuple."""

        hypothesis.set_observed_numbers((-1, 0, 1, 2, 3))
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == (-1, 0, 1, 2, 3)
```

### test_int_set

- **Description**: Test the `observed_numbers` parameter with an integer set.
- **Code Snippet**:
```
def test_int_set(self, hypothesis):
        """ Test the `observed_numbers` parameter with an integer set."""

        hypothesis.set_observed_numbers({-1, 0, 1, 2, 3})
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == {-1, 0, 1, 2, 3}
```

### test_float

- **Description**: Test the `observed_numbers` parameter with a float.
- **Code Snippet**:
```
def test_float(self, hypothesis):
        """ Test the `observed_numbers` parameter with a float."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(123.45)
            hypothesis.validate_observed_numbers()
```

### test_float_list

- **Description**: Test the `observed_numbers` parameter with a float list.
- **Code Snippet**:
```
def test_float_list(self, hypothesis):
        """ Test the `observed_numbers` parameter with a float list."""

        hypothesis.set_observed_numbers([-1.0, 0.0, 1.0, 2.0, 3.0])
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == [-1.0, 0.0, 1.0, 2.0, 3.0]
```

### test_float_tuple

- **Description**: Test the `observed_numbers` parameter with a float tuple.
- **Code Snippet**:
```text
def test_float_tuple(self, hypothesis):
        """ Test the `observed_numbers` parameter with a float tuple."""

        hypothesis.set_observed_numbers((-1.0, 0.0, 1.0, 2.0, 3.0))
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == (-1.0, 0.0, 1.0, 2.0, 3.0)
```

### test_float_set

- **Description**: Test the `observed_numbers` parameter with a float set.
- **Code Snippet**:
```text
def test_float_set(self, hypothesis):
        """ Test the `observed_numbers` parameter with a float set."""

        hypothesis.set_observed_numbers({-1.0, 0.0, 1.0, 2.0, 3.0})
        hypothesis.validate_observed_numbers()
        assert hypothesis.numbers == {-1.0, 0.0, 1.0, 2.0, 3.0}
```

### test_string

- **Description**: Test the `observed_numbers` parameter with a string.
- **Code Snippet**:
```text
def test_string(self, hypothesis):
        """ Test the `observed_numbers` parameter with a string."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers("123")
            hypothesis.validate_observed_numbers()
```

### test_string_list

- **Description**: Test the `observed_numbers` parameter with a string list.
- **Code Snippet**:
```text
def test_string_list(self, hypothesis):
        """ Test the `observed_numbers` parameter with a string list."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers(["-1", "0", "1", "2", "3"])
            hypothesis.validate_observed_numbers()
```

### test_dict

- **Description**: Test the `observed_numbers` parameter with a dictionary.
- **Code Snippet**:
```text
def test_dict(self, hypothesis):
        """ Test the `observed_numbers` parameter with a dictionary."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
            hypothesis.validate_observed_numbers()
```

### test_mixed_types

- **Description**: Test the `observed_numbers` parameter with mixed types.
- **Code Snippet**:
```text
def test_mixed_types(self, hypothesis):
        """ Test the `observed_numbers` parameter with mixed types."""

        with pytest.raises(RandomGenTypeError):
            hypothesis.set_observed_numbers([-1, 0.0, "1", 2.0, 3])
            hypothesis.validate_observed_numbers()
```

### test_mixed_numbers

- **Description**: Test the `observed_numbers` parameter with mixed numbers.
- **Code Snippet**:
```text
hypothesis.set_observed_numbers([-1, 0, 1, 2.0, 3])
hypothesis.validate_observed_numbers()
assert hypothesis.numbers == [-1, 0, 1, 2.0, 3]
```
 

## TestChiSquareParamProbabilities
**Description**: Test the `expected_probabilities` parameter.

### test_none
- **Description**: Test the `expected_probabilities` parameter with None.
- **Code Snippet**:
```
with pytest.raises(RandomGenTypeError):
    hypothesis.set_observed_numbers(None)
    hypothesis.validate_observed_numbers()
```

### test_empty
- **Description**: Test the `expected_probabilities` parameter with an empty list.
- **Code Snippet**:
```
with pytest.raises(RandomGenEmptyError):
    hypothesis.set_observed_numbers([])
    hypothesis.validate_observed_numbers()
```

### test_int
- **Description**: Test the `expected_probabilities` parameter with an integer.
- **Code Snippet**:
```
with pytest.raises(RandomGenTypeError):
    hypothesis.set_observed_numbers(123)
    hypothesis.validate_observed_numbers()
```

### test_int_list
- **Description**: Test the `expected_probabilities` parameter with an integer list.
- **Code Snippet**:
```
hypothesis.set_observed_numbers([-1, 0, 1, 2, 3])
hypothesis.validate_observed_numbers()
assert hypothesis.numbers == [-1, 0, 1, 2, 3]
```

### test_int_tuple
- **Description**: Test the `expected_probabilities` parameter with an integer tuple.
- **Code Snippet**:
```
hypothesis.set_observed_numbers((-1, 0, 1, 2, 3))
hypothesis.validate_observed_numbers()
assert hypothesis.numbers == (-1, 0, 1, 2, 3)
```

### test_int_set
- **Description**: Test the `expected_probabilities` parameter with an integer set.
- **Code Snippet**:
```
hypothesis.set_observed_numbers({-1, 0, 1, 2, 3})
hypothesis.validate_observed_numbers()
assert hypothesis.numbers == {-1, 0, 1, 2, 3}
```

### test_float
- **Description**: Test the `expected_probabilities` parameter with a float.
- **Code Snippet**:
```
with pytest.raises(RandomGenTypeError):
    hypothesis.set_observed_numbers(123.45)
    hypothesis.validate_observed_numbers()
```

### test_float_list
- **Description**: Test the `expected_probabilities` parameter with a float list.
- **Code Snippet**:
```
hypothesis.set_observed_numbers([-1.0, 0.0, 1.0, 2.0, 3.0])
hypothesis.validate_observed_numbers()
assert hypothesis.numbers == [-1.0, 0.0, 1.0, 2.0, 3.0]
```

### test_float_tuple
- **Description**: Test the `expected_probabilities` parameter with a float tuple.
- **Code Snippet**:
```
hypothesis.set_observed_numbers((-1.0, 0.0, 1.0, 2.0, 3.0))
hypothesis.validate_observed_numbers()
assert hypothesis.numbers == (-1.0, 0.0, 1.0, 2.0, 3.0)
```

### test_float_set
- **Description**: Test the `expected_probabilities` parameter with a float set.
- **Code Snippet**:
```
hypothesis.set_observed_numbers({-1.0, 0.0, 1.0, 2.0, 3.0})
hypothesis.validate_observed_numbers()
assert hypothesis.numbers == {-1.0, 0.0, 1.0, 2.0, 3.0}
```

### test_string
- **Description**: Test the `expected_probabilities` parameter with a string.
- **Code Snippet**:
```
with pytest.raises(RandomGenTypeError):
    hypothesis.set_observed_numbers("123")
    hypothesis.validate_observed_numbers()
```

### test_string_list
- **Description**: Test the `expected_probabilities` parameter with a string list.
- **Code Snippet**:
```
with pytest.raises(RandomGenTypeError):
    hypothesis.set_observed_numbers(["-1", "0", "1", "2", "3"])
    hypothesis.validate_observed_numbers()
```

### test_dict
- **Description**: Test the `expected_probabilities` parameter with a dictionary.
- **Code Snippet**:
```
with pytest.raises(RandomGenTypeError):
    hypothesis.set_observed_numbers({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
    hypothesis.validate_observed_numbers()
```

### test_mixed_types
- **Description**: Test the `expected_probabilities` parameter with mixed types.
- **Code Snippet**:
```
With pytest.raises(RandomGenTypeError):
    hypothesis.set_observed_numbers([-1, 0.0, "1", 2.0, 3])
    hypothesis.validate_observed_numbers()
```

### test_mixed_numbers
- **Description**: Test the `expected_probabilities` parameter with mixed numbers.
- **Code Snippet**:
```
hypothesis.set_observed_numbers([-1, 0, 1, 2.0, 3])
hypothesis.validate_observed_numbers()
assert hypothesis.numbers == [-1, 0, 1, 2.0, 3]
```

## TestChiSquareFunctional
**Description**: Test the functional aspects of the ChiSquareTest class.

### test_chi_square_pass
- **Description**: Test the ChiSquareTest class with a passing test.
- **Code Snippet**:
```
(
    hypothesis
    .set_observed_numbers([1, 1, 1, 2, 2, 2])
    .set_expected_probabilities([0.5, 0.5])
    .calc()
)

assert hypothesis.is_null() is True
```

### test_chi_square_fail
- **Description**: Test the ChiSquareTest class with a failing test.
- **Code Snippet**:
```
(
    hypothesis
    .set_observed_numbers([1, 1, 1, 2, 2, 2])
    .set_expected_probabilities([0.5, 0.5])
    .calc()
)

assert hypothesis.is_null() is True

def test_chi_square_fail(self, hypothesis):
""" Test the ChiSquareTest class with a failing test."""

(
    hypothesis
    .set_observed_numbers([1, 1, 1, 2, 2, 2])
    .set_expected_probabilities([0.1, 0.9])
    .calc()
)

assert hypothesis.is_null() is False
```
