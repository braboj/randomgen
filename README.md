[![Test Application](https://github.com/braboj/randomgen/actions/workflows/test_application.yml/badge.svg)](https://github.com/braboj/randomgen/actions/workflows/test_application.yml)
[![Deploy Image](https://github.com/braboj/randomgen/actions/workflows/deploy_image.yml/badge.svg)](https://github.com/braboj/randomgen/actions/workflows/deploy_image.yml)
[![Deploy Image](https://github.com/braboj/randomgen/actions/workflows/deploy_image.yml/badge.svg)](https://github.com/braboj/randomgen/actions/workflows/deploy_image.yml)

# Overview

This project is a simple REST API that generates random numbers. The project is
written in Python and uses the Flask framework to create the REST API. The
project is distributed as a Docker image, so you can run it on any platform that
supports Docker.

# Installation

To get started, you need to install Docker. You can find the installation
instructions [here](https://docs.docker.com/engine/install/). After that, 
you can run the following command to get the project image:

```bash
docker pull braboj/randomgen:latest
```

And finally, you can run the following command to start the project:

```bash
docker run -p 8080:8080 braboj/randomgen:latest
```

To access the project, open your browser and go to 
[http://localhost:8080](http://localhost:8080). A simple page will be 
displayed with the endpoints available. As a quick example, use the 
following link to create 100 random numbers:

```text
http://localhost:8080/api/v1/randomgen?numbers=100
```

# Next Steps
 - For more information, you can check [RandomGen Project Pages](https://braboj.github.io/randomgen/).
 - To contribute, please visit [Contributing](CONTRIBUTING.md)
 - To leave feedback, please visit [Discussions](https://github.com/braboj/randomgen/discussions/landing)
