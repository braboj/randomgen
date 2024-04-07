# Endpoints Module Tests

## test_endpoint_v1_randomgen_pos


- **Description**: Test the randomgen v1 endpoint with positive scenarios. 

- **Code Snippet**:

```text
for num in (1, 1000, 10000):
    self.api.randomgen_endpoint(RandomGenV1, num)
  ```

## test_endpoint_api_v1_randomgen_neg
- **Description**: Test the randomgen v1 endpoint with negative scenarios.
- **Code Snippet**:

```text
# Test the RandomGenMinError exception
with pytest.raises(RandomGenMinError):
    for num in (-1, 0):
        self.api.randomgen_endpoint(RandomGenV1, num)

# Test the RandomGenMaxError exception
with pytest.raises(RandomGenMaxError):
    for num in (10001,):
        self.api.randomgen_endpoint(RandomGenV1, num)
  ```

## test_endpoint_v2_randomgen_pos

- **Description**: Test the randomgen v2 endpoint with positive scenarios. 
- **Code Snippet**:

```text
for num in (1, 1000, 10000):
    self.api.randomgen_endpoint(RandomGenV2, num)
```

## test_endpoint_api_v2_randomgen_neg
- **Description**: Test the randomgen v2 endpoint with negative scenarios.
- **Code Snippet**:

```text
# Test the RandomGenMinError exception
with pytest.raises(RandomGenMinError):
    for num in (-1, 0):
        self.api.randomgen_endpoint(RandomGenV2, num)

# Test the RandomGenMaxError exception
with pytest.raises(RandomGenMaxError):
    for num in (10001,):
        self.api.randomgen_endpoint(RandomGenV2, num)
```

## test_endpoint_api_config_pos

- **Description**: Test the configuration endpoin in positive scenarios.
- **Code Snippet**:
```text
# Configuration endpoint
self.api.config_endpoint(numbers=[1, 2, 3],
                         probabilities=[0.2, 0.2, 0.6])

assert self.api.config['NUMBERS'] == [1, 2, 3]
assert self.api.config['PROBABILITIES'] == [0.2, 0.2, 0.6]
  ```

## test_endpoint_api_config_neg
- **Description**: Test the configuration endpoint with negative scenarios.
- **Code Snippet**:
```text
with pytest.raises(RandomGenMismatchError):
    self.api.config_endpoint(numbers=[1, 2, 3],
                             probabilities=[0.2, 0.2, 0.6, 0.1])

with pytest.raises(RandomGenMismatchError):
    self.api.config_endpoint(numbers=[1, 2, 3],
                             probabilities=[0.2, 0.2])

with pytest.raises(RandomGenEmptyError):
    self.api.config_endpoint(numbers=[], probabilities=[])

with pytest.raises(RandomGenProbabilityNegativeError):
    self.api.config_endpoint(numbers=[1, 2, 3],
                             probabilities=[0.2, 0.2, -0.6])

with pytest.raises(RandomGenProbabilitySumError):
    self.api.config_endpoint(numbers=[1, 2, 3],
                             probabilities=[0.2, 0.2, 0.5])

with pytest.raises(RandomGenTypeError):
    self.api.config_endpoint(numbers=1, probabilities=0.2)

with pytest.raises(RandomGenTypeError):
    self.api.config_endpoint(numbers=[1, 2, 3], probabilities=0.2)

with pytest.raises(RandomGenTypeError):
    self.api.config_endpoint(numbers=1, probabilities=[0.2, 0.2, 0.6])
  ```

## test_endpoint_api_reset

- **Description**: Test the reset endpoint.
- **Code Snippet**:
```text
self.api.config_endpoint(
    numbers=[1, 2, 3],
    probabilities=[0.2, 0.2, 0.6]
)

assert self.api.config['NUMBERS'] == [1, 2, 3]
assert self.api.config['PROBABILITIES'] == [0.2, 0.2, 0.6]

self.api.reset_endpoint()

assert self.api.config['NUMBERS'] == DEFAULT_NUMBERS
assert self.api.config['PROBABILITIES'] == DEFAULT_PROBABILITIES
```
