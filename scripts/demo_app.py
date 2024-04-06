from randomgen.core import RandomGenV1, RandomGenV2
from randomgen.hypothesis import ChiSquareTest
from flask import Flask, jsonify, request
from randomgen.histogram import Histogram


###############################################################################
# Application
###############################################################################

app = Flask(__name__)
app.numbers = [-1, 0, 1, 2, 3]
app.probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
app.max_numbers = 10000


###############################################################################
# Helpers
###############################################################################

def generate_random_numbers(randomgen, amount, version=1):
    # Check if the number of items to be generated is within the limit
    if amount > app.max_numbers:
        return jsonify({'error': 'Amount of numbers cannot exceed 1000'})

    # Generate random numbers
    random_numbers = [randomgen.next_num() for _ in range(amount)]

    # Expected distribution
    expected = dict(zip(app.numbers, app.probabilities))

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
        .set_expected_probabilities(app.probabilities)
        .calc()
    )

    # Prepare the response
    response = {

        'version': version,
        'numbers': random_numbers,

        "quality": {
            "chi_square_test":
                {
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


###############################################################################
# Event handlers
###############################################################################

# Global error handler
@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({'error': str(e)}), 500


###############################################################################
# Endpoints
###############################################################################

@app.get('/')
def hello_world():
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
            <li> POST /api/config (see documentation) </li>
        </ul>
    
        """
    )

    return body


@app.post('/api/config')
def api_config():
    app.numbers = request.json['numbers']
    app.probabilities = request.json['probabilities']
    return jsonify({'numbers': app.numbers, 'probabilities': app.probabilities})


# A route to get the configuration of the random number generator
@app.get('/api/v1/randomgen')
def api_v1_generate_numbers():
    # Query: /api/v1/randomgen?numbers=10

    # Parse the query parameter amount
    amount = request.args.get('numbers', default=1, type=int)

    # Generate random numbers from -1 to 3 using a custom distribution
    rg = (
        RandomGenV1()
        .set_numbers(app.numbers)
        .set_probabilities(app.probabilities)
        .validate()
    )

    return generate_random_numbers(rg, amount, version=1)


@app.get('/api/v2/randomgen')
def api_v2_generate_numbers():
    # Query: /api/v2/randomgen?numbers=10

    # Parse the query parameter amount
    amount = request.args.get('numbers', default=1, type=int)

    # Create the random number generator object
    rg = (
        RandomGenV2()
        .set_numbers(app.numbers)
        .set_probabilities(app.probabilities)
        .validate()
    )

    return generate_random_numbers(rg, amount, version=2)


if __name__ == '__main__':
    app.run(debug=False)
