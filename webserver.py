import requests
from flask import Flask, jsonify, request
from randomgen.core import RandomGenV1, RandomGenV2

app = Flask(__name__)


# A simple route that returns a string
@app.get('/')
def hello_world():
    return 'Hello, World!'


@app.get('/api/v1/randomgen')
def api_v1_numbers():

    # Query: /api/v1/randomgen?amount=10

    amount = request.args.get('amount', default=1, type=int)
    random_number = (
        RandomGenV1()
        .set_numbers([-1, 0, 1, 2, 3])
        .set_probabilities([0.01, 0.3, 0.58, 0.1, 0.01])
        .validate()
    )

    numbers = [random_number.next_num() for _ in range(amount)]

    return jsonify({'number': numbers})


@app.get('/api/v2/randomgen')
def api_v2_numbers():

    # Query: /api/v2/randomgen?amount=10

    amount = request.args.get('amount', default=1, type=int)
    random_number = (
        RandomGenV2()
        .set_numbers([-1, 0, 1, 2, 3])
        .set_probabilities([0.01, 0.3, 0.58, 0.1, 0.01])
        .validate()
    )

    numbers = [random_number.next_num() for _ in range(amount)]

    return jsonify({'number': numbers})


if __name__ == '__main__':
    app.run(debug=True)
