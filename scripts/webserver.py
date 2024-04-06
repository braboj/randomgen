from flask import Flask, jsonify, request
from randomgen.core import RandomGenV1, RandomGenV2
from randomgen.hypothesis import ChiSquareTest
from randomgen.histogram import Histogram

DEFAULT_NUMBERS = [-1, 0, 1, 2, 3]
DEFAULT_PROBABILITIES = [0.01, 0.3, 0.58, 0.1, 0.01]
MAX_NUMBERS = 10000


class RandomGeneratorApp(Flask):
    """Random Number Generator REST API.

    This class wraps the Flask application and provides a REST API for
    generating random numbers based on a given set of numbers and their
    probabilities. The API also provides a way to configure the numbers and
    probabilities used for generating random numbers.

    Attributes:

        debug: A boolean flag to enable or disable debugging.

    Endpoints:
    - GET /api/v1/randomgen: Generate random numbers using RandomGenV1.
    - GET /api/v2/randomgen: Generate random numbers using RandomGenV2.
    - /api/config: Configure the numbers and probabilities.
    - /api/reset: Reset the configuration to the default values.

    """

    def __init__(self, debug=False):

        # Create the Flask application
        super().__init__("randomgen")

        # Set the configuration
        self.setup_config()

        # Register the routes
        self.register_routes()

    def setup_config(self):
        """ Configure the Flask application using the default values. """

        self.config['MAX_NUMBERS'] = MAX_NUMBERS
        self.config['NUMBERS'] = DEFAULT_NUMBERS
        self.config['PROBABILITIES'] = DEFAULT_PROBABILITIES

    def generate_random_numbers(self, randomgen, amount):
        """ Generate random numbers using the given random number generator. """

        # Check if the amount is negative or zero
        if amount <= 0:
            return jsonify(
                {'error': 'Amount of numbers must be greater than 0'}), 400

        # Check if the amount exceeds the maximum limit
        elif amount > self.config['MAX_NUMBERS']:
            return jsonify(
                {'error': f'Numbers cannot exceed {MAX_NUMBERS}'}), 400

        # Generate random numbers
        random_numbers = [randomgen.next_num() for _ in range(amount)]

        # Expected distribution
        expected = dict(zip(
            self.config['NUMBERS'],
            self.config['PROBABILITIES'])
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
            .set_expected_probabilities(self.config['PROBABILITIES'])
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

    @staticmethod
    def home_endpoint():
        """ Home endpoint. """

        body = (
            """
            <h1>Random Number Generator API</h1>

            Author: Branimir Georgiev

            <p>
            The fairness of the random number generator is tested using the 
            Chi-Square test. Larger numbers of generated random numbers will 
            result in a more accurate test.
            </p>

            <p>Endpoints:</p>

            <ul>
                <li> GET /api/v1/randomgen?numbers=1000 </li>
                <li> GET /api/v2/randomgen?numbers=1000 </li>
                <li> POST /api/config {"numbers":[1, 2], "probabilities":[0.5, 0.5]}</li>
                <li> POST /api/reset </li>
            </ul>

            """
        )

        return body

    def randomgen_endpoint(self, randomgen_version):
        """ Generate random numbers using the given version of RandomGen. """

        # Get the quantity of numbers to generate
        amount = request.args.get('numbers', default=1, type=int)

        # Create the random number generator
        rg = (
            randomgen_version()
            .set_numbers(self.config['NUMBERS'])
            .set_probabilities(self.config['PROBABILITIES'])
            .validate()
        )

        # Generate random numbers
        return self.generate_random_numbers(rg, amount)

    def config_endpoint(self):
        """ Configure the numbers and probabilities. """

        self.config['NUMBERS'] = request.json['numbers']
        self.config['PROBABILITIES'] = request.json['probabilities']

        return jsonify({
            'numbers': self.config['NUMBERS'],
            'probabilities': self.config['PROBABILITIES']}
        )

    def reset_endpoint(self):
        """ Reset the configuration to the default values. """

        self.setup_config()

        return jsonify({
            'numbers': self.config['NUMBERS'],
            'probabilities': self.config['PROBABILITIES']}
        )

    def register_routes(self):
        """ Register the routes for the API. """

        @self.route('/')
        def hello_world():
            return self.home_endpoint()

        @self.get('/api/v1/randomgen')
        def api_v1():
            return self.randomgen_endpoint(randomgen_version=RandomGenV1)

        @self.get('/api/v2/randomgen')
        def api_v2():
            return self.randomgen_endpoint(randomgen_version=RandomGenV2)

        @self.post('/api/config')
        def api_config():
            return self.config_endpoint()

        @self.get('/api/reset')
        def api_reset():
            return self.reset_endpoint()

        @self.errorhandler(Exception)
        def handle_error(e):
            return jsonify({'error': str(e)}), 500
