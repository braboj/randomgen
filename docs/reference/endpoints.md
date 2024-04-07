# Endpoints Module Reference

## RandomGenRestApi

This class implements the REST API logic for the RandomGen project. The 
implementation is not aware of the web framework that is being used. It 
performs the business logic and some checks before returning the results to 
the web framework.

Attributes:
- config (dict): The configuration dict used by the API.

### setup_config()

Configure the Flask application using the default values.

Returns:
- dict: The configuration dict after the change.

### generate_random_numbers()

Generate random numbers using the given random number generator.

Args:

- randomgen: The random number generator object.
- quantity: The quantity of random numbers to generate.

Returns:

- dict: A dictionary containing the generated random numbers and the
- results of the Chi-Square test.

### home_endpoint()

Return the HTML body of the home page. This is the default page of the API.

Returns:

- str: The HTML body of the home page.

### randomgen_endpoint()

Generate random numbers using the given version of RandomGen.

Args:

- randomgen_type: The concrete class of RandomGen to use.
- numbers: The quantity of random numbers to generate.

Returns:

- dict: A dictionary containing the generated random numbers and the
- results of the Chi-Square test.

### config_endpoint()

Configure the numbers and probabilities.

Returns:

- dict: A dictionary containing the new numbers and probabilities.

### reset_endpoint()

Reset the configuration to the default values.

Returns:

- dict: A dictionary containing the default numbers and probabilities.

