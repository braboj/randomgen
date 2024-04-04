import requests
from flask import Flask, jsonify, request
from randomgen.core import RandomGenV1, RandomGenV2
from randomgen.hypothesis import ChiSquareTest
from collections import OrderedDict
from randomgen.errors import RandomGenError

app = Flask(__name__)
app.numbers = [-1, 0, 1, 2, 3]
app.probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]


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
            <li> /api/v1/randomgen?number=1000 </li>
            <li> /api/v2/randomgen?number=1000 </li>
        </ul>
    
        """
    )

    return body

@app.post('/api/config')
def api_config():
    app.numbers = request.json['numbers']
    app.probabilities = request.json['probabilities']

    return jsonify({'numbers': app.numbers, 'probabilities': app.probabilities})


@app.get('/api/v1/randomgen')
def api_v1_generate_numbers():

    # Query: /api/v1/randomgen?amount=10
    response = {}

    # Parse the query parameter amount
    amount = request.args.get('number', default=1, type=int)

    # Generate random numbers from -1 to 3 using a custom distribution
    random_number = (
        RandomGenV1()
        .set_numbers(app.numbers)
        .set_probabilities(app.probabilities)
        .validate()
    )

    # Generate the random numbers
    random_numbers = [random_number.next_num() for _ in range(amount)]

    # Create the hypothesis test object
    hypothesis = (
        ChiSquareTest()
        .set_numbers(random_numbers)
        .set_probabilities(app.probabilities)
        .calculate()
    )

    # Return the random numbers as JSON
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


@app.get('/api/v2/randomgen')
def api_v2_generate_numbers():

    # Query: /api/v1/randomgen?amount=10

    # Parse the query parameter amount
    amount = request.args.get('number', default=1, type=int)

    # Generate random numbers from -1 to 3 using a custom distribution
    random_number = (
        RandomGenV1()
        .set_numbers(app.numbers)
        .set_probabilities(app.probabilities)
        .validate()
    )

    # Generate the random numbers
    random_numbers = [random_number.next_num() for _ in range(amount)]

    # Create the hypothesis test object
    hypothesis = (
        ChiSquareTest()
        .set_numbers(random_numbers)
        .set_probabilities(app.probabilities)
        .calculate()
    )

    # Return the random numbers as JSON
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

if __name__ == '__main__':
    app.run(debug=True)
