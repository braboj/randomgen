import requests

# Endpoint URL
url = 'http://127.0.0.1:5000/api/config'

# Sample data
data = {
    'numbers': [1, 2, 3],
    'probabilities': [0.2, 0.2, 0.6]
}

# Send a POST request
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("Response from server:", response.json())
else:
    print("Error:", response.status_code)

# Endpoint URL
url = 'http://127.0.0.1:5000/api/v1/randomgen'

# Query parameters
params = {'numbers': 10}

# Send a GET request
response = requests.get(url, params=params)

# Check the response
if response.status_code == 200:
    print("Response from server:", response.json())

else:
    print("Error:", response.status_code)
