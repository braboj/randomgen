# Routing Module Reference

This module implements the routing for the application. It defines the routes
the business logic layer and the error handlers. The routing is implemented
using the Flask framework.

## hello_world()

**Decorated with:** @route

Route for the default home page.

Returns:
- str: The home page message.

## api_v1_randomgen()

**Decorated with:** @get

Route for the /api/v1/randomgen endpoint.

Returns:
- flask.Response: The response from the randomgen endpoint.

## api_v2_randomgen()

**Decorated with:** @get

Route for the /api/v2/randomgen endpoint.

Returns:
- flask.Response: The response from the randomgen endpoint.

## api_config()

**Decorated with:** @post

Route for the /api/config endpoint.

Returns:
- flask.Response: The response from the config endpoint.

## api_reset()

**Decorated with:** @get

Route for the /api/reset endpoint.

Returns:
- flask.Response: The response from the reset endpoint.

## handle_error()

**Decorated with:** @errorhandler

Error handler for the application.

Returns:
- flask.Response: The error response.

