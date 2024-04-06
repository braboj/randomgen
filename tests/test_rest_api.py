# encoding: utf-8
import pytest
import requests
import threading
from randomgen.app import RandomNumberGeneratorApp


@pytest.fixture(autouse=True)
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

    def test_endpoint_api_v1_randomgen(self):

        # Endpoint URL
        url = self.base_url + '/api/v1/randomgen'

        # Query parameters
        params = {'numbers': 1000}

        # Send a GET request
        response = requests.get(url, params=params)

        # Check the response
        assert response.status_code == 200

    def test_endpoint_api_v2_randomgen(self):

        # Endpoint URL
        url = self.base_url + '/api/v2/randomgen'

        # Query parameters
        params = {'numbers': 1000}

        # Send a GET request
        response = requests.get(url, params=params)

        # Check the response
        assert response.status_code == 200

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


if __name__ == "__main__":
    pytest.main()
