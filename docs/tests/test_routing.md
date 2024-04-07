# Routing Module Tests

## TestRestApiRouting
**Description**: Test the REST API routing.


### test_endpoint_api_v1_randomgen_pos

- **Description**: Test the /api/v1/randomgen endpoint with positive numbers.
- **Code Snippet**:
```text
# Endpoint URL
url = self.base_url + '/api/v1/randomgen'

for num in (1, 1000, 10000):
    # Query parameters
    params = {'numbers': num}

    # Send a GET request
    response = requests.get(url, params=params)

    # Check the response
    assert response.status_code == 200
```

### test_endpoint_api_v1_randomgen_neg

- **Description**: Test the /api/v1/randomgen endpoint with negative numbers.
- **Code Snippet**:
```text
# Endpoint URL
url = self.base_url + '/api/v1/randomgen'

for num in (-1, 0, 10001,):
    # Query parameters
    params = {'numbers': num}

    # Send a GET request
    response = requests.get(url, params=params)

    # Check the response
    assert response.status_code == 500
```

### test_endpoint_api_v2_randomgen_pos

- **Description**: Test the /api/v2/randomgen endpoint with positive numbers.
- **Code Snippet**:
```text
# Endpoint URL
url = self.base_url + '/api/v2/randomgen'

for num in (1, 10000):
    # Query parameters
    params = {'numbers': num}

    # Send a GET request
    response = requests.get(url, params=params)

    # Check the response
    assert response.status_code == 200
```

### test_endpoint_api_v2_randomgen_neg

- **Description**: Test the /api/v2/randomgen endpoint with negative numbers.
- **Code Snippet**:
```text
# Endpoint URL
url = self.base_url + '/api/v2/randomgen'

for num in (-1, 0, 10001,):
    # Query parameters
    params = {'numbers': num}

    # Send a GET request
    response = requests.get(url, params=params)

    # Check the response
    assert response.status_code == 500
```

### test_endpoint_api_config

- **Description**: Test the /api/config endpoint.
- **Code Snippet**:
```text
# Endpoint URL
url = self.base_url + '/api/config'

# Sample data
data = {
    'numbers': [1, 2, 3],
    'probabilities': [0.2, 0.2, 0.6]
}

# Send a POST request
response = requests.post(url, json=data)

# Convert response to JSON
response_json = response.json()

# Check the response
assert response_json['numbers'] == data['numbers']
assert response_json['probabilities'] == data['probabilities']

# Check the response
assert response.status_code == 200
```

### test_endpoint_api_reset

- **Description**: Test the /api/reset endpoint.
- **Code Snippet**:
```text
# Change the configuration
url = self.base_url + '/api/config'
data = {
    'numbers': [1, 2, 3],
    'probabilities': [0.2, 0.2, 0.6]
}

# Send a POST request
response = requests.post(url, json=data)
response_json = response.json()

# Check the response
assert response_json['numbers'] == data['numbers']
assert response_json['probabilities'] == data['probabilities']

# Tested Endpoint URL
url = self.base_url + '/api/reset'

# Send a POST request
response = requests.post(url, json=data)
response_json = response.json()

# Check the response
assert response_json['numbers'] == DEFAULT_NUMBERS
assert response_json['probabilities'] == DEFAULT_PROBABILITIES

# Check the response
assert response.status_code == 200
```
