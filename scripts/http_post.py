import requests

# Endpoint URL
url = 'http://127.0.0.1:5000/api/config'

# Sample data
data = {
    'numbers': [1, 2, 3, 3, 3],  # Sample numbers
    'probabilities': [0.2, 0.2, 0.6]  # Corresponding probabilities
}

# Send a POST request
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("Response from server:", response.json())
else:
    print("Error:", response.status_code)
