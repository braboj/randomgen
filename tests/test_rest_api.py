import requests
from http import HTTPStatus
import pytest

class TestRestAPI(object):

    def test_CONFIG_STATUS(self):

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
        assert response.status_code == HTTPStatus.OK


    def test_RANDOMGEN_V1_STATUS(self):

        # Endpoint URL
        url = 'http://127.0.0.1:5000/api/v1/randomgen'

        # Query parameters
        params = {'number': 10}

        # Send a GET request
        response = requests.get(url, params=params)

        # Check the response
        assert response.status_code == HTTPStatus.OK


if __name__ == '__main__':
    pytest.main()