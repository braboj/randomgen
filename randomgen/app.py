from flask import Flask, jsonify, request
from randomgen.core import RandomGenV1, RandomGenV2
from randomgen.hypothesis import ChiSquareTest
from randomgen.histogram import Histogram


class RandomNumberGeneratorApp(object):
    """Random Number Generator REST API.

    This class wraps the Flask application and provides a REST API for
    generating random numbers based on a given set of numbers and their
    probabilities. The API also provides a way to configure the numbers and
    probabilities used for generating random numbers.

    Attributes:
        app: The Flask application.
        debug: A boolean flag to enable or disable debugging.

    Endpoints:
    - GET /api/v1/randomgen: Generate random numbers using RandomGenV1.
    - GET /api/v2/randomgen: Generate random numbers using RandomGenV2.
    - /api/config: Configure the numbers and probabilities.

    """

    def __init__(self, debug=False):

        # Create the Flask application
        self.app = Flask(__name__)

        # Set the debug flag
        self.debug = debug

        # Setup the configuration
        self.setup_config()

        # Register the routes
        self.register_routes()

    def setup_config(self):
        """ Configure the Flask application using the default values. """

        self.app.config['MAX_NUMBERS'] = 10000
        self.app.config['NUMBERS'] = [-1, 0, 1, 2, 3]
        self.app.config['PROBABILITIES'] = [0.01, 0.3, 0.58, 0.1, 0.01]

    def generate_random_numbers(self, randomgen, amount):
        """ Generate random numbers using the given random number generator. """

        # Check if the amount is within the limits
        if amount > self.app.config['MAX_NUMBERS']:
            return jsonify(
                {'error': 'Amount of numbers cannot exceed 1000'}), 400

        # Generate random numbers
        random_numbers = [randomgen.next_num() for _ in range(amount)]

        # Expected distribution
        expected = dict(zip(
                self.app.config['NUMBERS'],
                self.app.config['PROBABILITIES'])
        )

        # Observed distribution
        observed = (
            Histogram()
            .set_numbers(random_numbers)
            .calc()
        )

        # Chi-Square test to check the quality of the random number generator
        hypothesis = (
            ChiSquareTest()
            .set_observed_numbers(random_numbers)
            .set_expected_probabilities(self.app.config['PROBABILITIES'])
            .calc()
        )

        # Prepare the response
        response = {
            'numbers': random_numbers,
            "quality": {
                "chi_square_test": {
                    'is_null': int(hypothesis.is_null()),
                    'chi_square': hypothesis.chi_square,
                    'p_value': hypothesis.p_value,
                    'df': hypothesis.df,
                },
                'expected_histogram': expected,
                'observed_histogram': observed,
            },
        }

        # Return the response
        return jsonify(response)

    def randomgen_endpoint(self, randomgen_version):
        """ Generate random numbers using the given version of RandomGen. """

        # Get the quantity of numbers to generate
        amount = request.args.get('numbers', default=1, type=int)

        # Create the random number generator
        rg = (
                randomgen_version()
                .set_numbers(self.app.config['NUMBERS'])
                .set_probabilities(self.app.config['PROBABILITIES'])
                .validate()
            )

        # Generate random numbers
        return self.generate_random_numbers(rg, amount)

    def config_endpoint(self):
        """ Configure the numbers and probabilities. """

        self.app.config['NUMBERS'] = request.json['numbers']
        self.app.config['PROBABILITIES'] = request.json['probabilities']

        return jsonify({
            'numbers': self.app.config['NUMBERS'],
            'probabilities': self.app.config['PROBABILITIES']}
        )

    def register_routes(self):
        """ Register the routes for the API. """

        @self.app.route('/')
        def hello_world():
            return "<h1>Welcome to the Random Number Generator API</h1>"

        @self.app.get('/api/v1/randomgen')
        def api_v1():
            return self.randomgen_endpoint(randomgen_version=RandomGenV1)

        @self.app.get('/api/v2/randomgen')
        def api_v2():
            return self.randomgen_endpoint(randomgen_version=RandomGenV2)

        @self.app.post('/api/config')
        def api_config():
            return self.config_endpoint()

        @self.app.errorhandler(Exception)
        def handle_error(e):
            return jsonify({'error': str(e)}), 500

    def run(self, host='127.0.0.1', port=5000):
        """ Run the Flask application. """
        self.app.run(debug=self.debug, host=host, port=port)


if __name__ == '__main__':
    rng_app = RandomNumberGeneratorApp(debug=True)
    rng_app.run()
