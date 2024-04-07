from flask import Flask, jsonify, request
from randomgen.core import RandomGenV1, RandomGenV2
from randomgen.endpoints import RandomGenRestApi

app = Flask(__name__)
app.rest_api = RandomGenRestApi()


@app.route('/')
def hello_world():
    """Route for the home page."""
    return app.rest_api.home_endpoint()


@app.get('/api/v1/randomgen')
def api_v1_randomgen():
    """Route for the /api/v1/randomgen endpoint."""

    # Parse the query parameter
    quantity = request.args.get('numbers', default=1, type=int)

    return jsonify(
        app.rest_api
        .randomgen_endpoint(
            randomgen_type=RandomGenV1,
            numbers=quantity
        )
    )


@app.get('/api/v2/randomgen')
def api_v2_randomgen():
    """Route for the /api/v2/randomgen endpoint."""

    # Parse the query parameter
    quantity = request.args.get('numbers', default=1, type=int)

    return jsonify(
        app.rest_api
        .randomgen_endpoint(
            randomgen_type=RandomGenV2,
            numbers=quantity
        )
    )


@app.post('/api/config')
def api_config():
    """Route for the /api/config endpoint."""

    numbers = request.json['numbers']
    probabilities = request.json['probabilities']
    return jsonify(
        app.rest_api.config_endpoint(
            numbers=numbers,
            probabilities=probabilities
        )
    )


@app.get('/api/reset')
def api_reset():
    """Route for the /api/reset endpoint."""
    return jsonify(
        app.rest_api.reset_endpoint()
    )


@app.errorhandler(Exception)
def handle_error(e):
    """Error handler for the application."""
    return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
