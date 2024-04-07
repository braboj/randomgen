# Histogram Module Tests

## TestHistogramParamNumbers
**Description**: Test the `numbers` parameter.

### `test_none`
- **Description**: Test the `numbers` parameter with None.
- **Code Snippet**:

```text
with pytest.raises(RandomGenTypeError):
    histogram.set_numbers(None)
    histogram.validate_numbers()
```

### `test_empty`

- **Description**: Test the `numbers` parameter with an empty list.
- **Code Snippet**:
```text
with pytest.raises(RandomGenEmptyError):
    histogram.set_numbers([])
    histogram.validate_numbers()
```

### `test_int`

- **Description**: Test the `numbers` parameter with an integer.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    histogram.set_numbers(123)
    histogram.validate_numbers()
```

### `test_int_list`

- **Description**: Test the `numbers` parameter with an integer list.
- **Code Snippet**:
```text
histogram.set_numbers([-1, 0, 1, 2, 3])
histogram.validate_numbers()
assert histogram._numbers == [-1, 0, 1, 2, 3]
```

### `test_int_tuple`

- **Description**: Test the `numbers` parameter with an integer tuple.
- **Code Snippet**:
```text
histogram.set_numbers((-1, 0, 1, 2, 3))
histogram.validate_numbers()
assert histogram._numbers == (-1, 0, 1, 2, 3)
```

### `test_int_set`

- **Description**: Test the `numbers` parameter with an integer set.
- **Code Snippet**:
```text
histogram.set_numbers({-1, 0, 1, 2, 3})
histogram.validate_numbers()
assert histogram._numbers == {-1, 0, 1, 2, 3}
```

### `test_float`

- **Description**: Test the `numbers` parameter with a float.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    histogram.set_numbers(123.45)
    histogram.validate_numbers()
```

### `test_float_list`

- **Description**: Test the `numbers` parameter with a float list.
- **Code Snippet**:
```text
histogram.set_numbers([-1.0, 0.0, 1.0, 2.0, 3.0])
histogram.validate_numbers()
assert histogram._numbers == [-1.0, 0.0, 1.0, 2.0, 3.0]
```

### `test_float_tuple`

- **Description**: Test the `numbers` parameter with a float tuple.
- **Code Snippet**:
```text
histogram.set_numbers((-1.0, 0.0, 1.0, 2.0, 3.0))
histogram.validate_numbers()
assert histogram._numbers == (-1.0, 0.0, 1.0, 2.0, 3.0)
```

### `test_float_set`

- **Description**: Test the `numbers` parameter with a float set.
- **Code Snippet**:
```text
histogram.set_numbers({-1.0, 0.0, 1.0, 2.0, 3.0})
histogram.validate_numbers()
assert histogram._numbers == {-1.0, 0.0, 1.0, 2.0, 3.0}
```

### `test_string`

- **Description**: Test the `numbers` parameter with a string.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    histogram.set_numbers("123")
    histogram.validate_numbers()
```

### `test_string_list`

- **Description**: Test the `numbers` parameter with a string list.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    histogram.set_numbers(["-1", "0", "1", "2", "3"])
    histogram.validate_numbers()
```

### `test_dict`

- **Description**: Test the `numbers` parameter with a dictionary.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    histogram.set_numbers({-1: 1, 0: 1, 1: 1, 2: 1, 3: 1})
    histogram.validate_numbers()
```

### `test__mixed_types`

- **Description**: Test the `numbers` parameter with mixed types.
- **Code Snippet**:
```text
with pytest.raises(RandomGenTypeError):
    histogram.set_numbers([-1, 0.0, "1", 2.0, 3])
    histogram.validate_numbers()
```

### `test__mixed_numbers`

- **Description**: Test the `numbers` parameter with mixed numbers.
- **Code Snippet**:
```text
histogram.set_numbers([-1, 0, 1, 2.0, 3])
histogram.validate_numbers()
assert histogram._numbers == [-1, 0, 1, 2.0, 3]

```

## TestHistogramFunctional
**Description**: Test the functional aspects of the `Histogram` class.


### test_from_dict

- **Description**: Test the `from_dict` method.
- **Code Snippet**:
```text
histogram.from_dict({-1: 0.01, 0: 0.3, 1: 0.58, 2: 0.1, 3: 0.01})
assert list(histogram.keys()) == [-1, 0, 1, 2, 3]
assert list(histogram.values()) == [0.01, 0.3, 0.58, 0.1, 0.01]
```

### test_calc

- **Description**: Test the `calc` method.
- **Code Snippet**:
```text
histogram.set_numbers([-1, -1, 0, 0, 1, 1,  2, 2, 3, 3])
histogram.calc()
assert list(histogram.keys()) == [-1, 0, 1, 2, 3]
assert list(histogram.values()) == [0.2, 0.2, 0.2, 0.2, 0.2]

```
