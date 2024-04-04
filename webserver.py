import requests
from flask import Flask, jsonify, request
from randomgen.core import RandomGenV1, RandomGenV2
from randomgen.hypothesis import ChiSquareTest
from collections import OrderedDict
from randomgen.errors import RandomGenError

app = Flask(__name__)
app.bins = [-1, 0, 1, 2, 3]
app.probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
app.max_numbers = 10000

@app.errorhandler(RandomGenError)
def handle_error(e):
    return jsonify({'error': str(e)}), 400

def handle_randomgen_request(randomgen, amount):

    if amount > app.max_numbers:
        return jsonify({'error': 'Amount of numbers cannot exceed 1000'})

    random_numbers = [randomgen.next_num() for _ in range(amount)]

    hypothesis = (
        ChiSquareTest()
        .set_numbers(random_numbers)
        .set_probabilities(app.probabilities)
        .calculate()
    )

    response = OrderedDict(
        {
        'version': 1,
        'distribution': app.probabilities,
        'is_fair': int(hypothesis.test()),
        'chi_square': hypothesis.chi_square,
        'p_value': hypothesis.p_value,
        'df': hypothesis.df,
        'numbers': random_numbers,
        }
    )

    return jsonify(response)


# A simple route that returns a string
@app.get('/')
def hello_world():

    body = (
        """
        <h1>Random Number Generator API</h1>
        
        Author: Branimir Georgiev
        
        <p>
        The fairness of the random number generator is tested using the Chi-Square test. Larger
        numbers of generated random numbers will result in a more accurate test.
        </p>
        
        <p>Endpoints:</p>
        
        <ul>
            <li> /api/v1/randomgen?numbers=1000 </li>
            <li> /api/v2/randomgen?numbers=1000 </li>
        </ul>
    
        """
    )

    return body

@app.post('/api/config')
def api_config():
    app.bins = request.json['bins']
    app.probabilities = request.json['probabilities']

    return jsonify({'bins': app.bins, 'probabilities': app.probabilities})


@app.get('/api/v1/randomgen')
def api_v1_generate_numbers():

    # Query: /api/v1/randomgen?amount=10
    response = {}

    # Parse the query parameter amount
    amount = request.args.get('numbers', default=1, type=int)

    # Generate random numbers from -1 to 3 using a custom distribution
    rg = (
        RandomGenV1()
        .set_bins(app.bins)
        .set_probabilities(app.probabilities)
        .validate()
    )

    return handle_randomgen_request(rg, amount)


@app.get('/api/v2/randomgen')
def api_v2_generate_numbers():

    # Query: /api/v1/randomgen?amount=10

    # Parse the query parameter amount
    amount = request.args.get('numbers', default=1, type=int)

    # Create the random number generator object
    rg = (
        RandomGenV1()
        .set_bins(app.bins)
        .set_probabilities(app.probabilities)
        .validate()
    )

    return handle_randomgen_request(rg, amount)

if __name__ == '__main__':
    app.run(debug=True)
