import requests

# Endpoint URL
url = 'http://127.0.0.1:5000/api/v1/randomgen?amount=10'

# Send a GET request
response = requests.get(url)

# Parse the response
if response.status_code == 200:
    print("Response from server:", response.json())

else:
    print("Error:", response.status_code)