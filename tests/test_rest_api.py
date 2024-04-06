# encoding: utf-8

from randomgen.app import (
    RandomNumberGeneratorApp,
    DEFAULT_NUMBERS,
    DEFAULT_PROBABILITIES
)

import pytest
import requests
import threading

@pytest.fixture(autouse=True, scope='module')
def run_app():
    app = RandomNumberGeneratorApp()
    webserver = threading.Thread(target=app.run)
    webserver.daemon = True
    webserver.start()
    yield webserver


###############################################################################

class TestRestApiIntegration(object):

    @classmethod
    def setup_class(cls):
        cls.base_url = 'http://127.0.0.1:5000'

    def test_endpoint_api_v1_randomgen_pos(self):

        # Endpoint URL
        url = self.base_url + '/api/v1/randomgen'

        for num in (1, 1000, 10000):

            # Query parameters
            params = {'numbers': num}

            # Send a GET request
            response = requests.get(url, params=params)

            # Check the response
            assert response.status_code == 200

    def test_endpoint_api_v1_randomgen_neg(self):

        # Endpoint URL
        url = self.base_url + '/api/v1/randomgen'

        for num in (-1, 0, 10001, ):

            # Query parameters
            params = {'numbers': num}

            # Send a GET request
            response = requests.get(url, params=params)

            # Check the response
            assert response.status_code == 400

    def test_endpoint_api_v2_randomgen_pos(self):

        # Endpoint URL
        url = self.base_url + '/api/v2/randomgen'

        for num in (1, 10000):

            # Query parameters
            params = {'numbers': num}

            # Send a GET request
            response = requests.get(url, params=params)

            # Check the response
            assert response.status_code == 200

    def test_endpoint_api_v2_randomgen_neg(self):

        # Endpoint URL
        url = self.base_url + '/api/v2/randomgen'

        for num in (-1, 0, 10001, ):

            # Query parameters
            params = {'numbers': num}

            # Send a GET request
            response = requests.get(url, params=params)

            # Check the response
            assert response.status_code == 400

    def test_endpoint_api_config(self):

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

    def test_endpoint_api_reset(self, run_app):

        # Change the configuration
        url = self.base_url + '/api/config'
        data = {
            'numbers': [1, 2, 3],
            'probabilities': [0.2, 0.2, 0.6]
        }
        response = requests.post(url, json=data)
        response_json = response.json()

        assert response_json['numbers'] == data['numbers']
        assert response_json['probabilities'] == data['probabilities']

        # Tested Endpoint URL
        url = self.base_url + '/api/reset'

        # Send a GET request
        response = requests.get(url)

        # Convert response to JSON
        response_json = response.json()

        # Check the response
        assert response_json['numbers'] == DEFAULT_NUMBERS
        assert response_json['probabilities'] == DEFAULT_PROBABILITIES

        # Check the response
        assert response.status_code == 200


if __name__ == "__main__":
    pytest.main()
