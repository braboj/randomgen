## Problem Statement

Given Random Numbers are [-1, 0, 1, 2, 3] and Probabilities are [0.01, 0.3, 
0.58, 0.1, 0.01] if we call nextNum() 100 times, we may get the following 
results. As the results are random, these particular results are unlikely.

```text
-1: 1 times
0: 22 times
1: 57 times
2: 20 times
3: 0 times
```

**Instructions:**

 - Write a random number generator that returns numbers based on the 
   probabilities provided.
 - Implement the method nextNum() and a minimal but effective set of unit tests.
 - Implement in the language of your choice, Python is preferred, but Java and 
   other languages are completely fine.
 - Make sure your code is exemplary, as if it was going to be shipped as part 
   of a production system.

You may use random.random() which returns a pseudo random number between 0 
and 1. 

```python
import random

class RandomGen(object):
  
  # Values that may be returned by next_num()
  _random_nums = []
  
  # Probability of the occurrence of random_nums
  _probabilities = []
  
def next_num(self):
    """
    Returns one of the randomNums. When this method is called multiple
    times over a long period, it should return the numbers roughly with
    the initialized probabilities.
    """
    pass 

```

## Solution Journal

### 1. Select the technology stack

- Language: Python 3.12+
- Testing: Pytest
- CI/CD: GitHub Actions
- Version Control: Git
- Documentation: MkDocs

### 2. Validate the data from the problem statement

Let's first check if the given numbers are correct. As QA engineer, the data
given is never trusted ;)

1. Is the length of random_nums and probabilities equal?
2. Is the sum of probabilities equal to 1?
3. Are all probabilities positive?

A manual check is enough for this task. 

1. Yes, the length of random_nums and probabilities is equal.
2. Yes, the sum of probabilities is equal to 1.
3. Yes, all probabilities are positive.

We can proceed with the implementation.

### 3. Questions, questions and more questions

We don't have any information on how the data is generated, for example, how 
many samples were taken to get the given distribution. Typically, this may lead
to skewed results due to under-sampling. Visually, our distribution looks like a
custom distribution.

![Custom_Distribution.png](assets/images/custom_distribution.png)

It doesn't seem to be a binomial distribution... 

![Binomial_Distribution.png](assets/images/binomial_distribution.png)

... or a Poisson distribution.

![Poisson_Distribution.png](assets/images/poisson_distribution.png)

We will assume that the given distribution is correct and proceed with the
implementation. We will test our implementation with a large number of samples
for fairness using the Chi-Squared test.

### 4. Prototyping the solution

```python
import random

class RandomGen(object):
    
  def __init__(self, random_nums, probabilities):
    self._random_nums = random_nums
    self._probabilities = probabilities
    
  def _validate_input(self):
     
    if len(self._random_nums) != len(self._probabilities):
      raise ValueError("Length of random_nums and probabilities should be equal")
    
    if sum(self._probabilities) != 1:
      raise ValueError("Sum of probabilities should be 1")
    
    if any(prob < 0 for prob in self._probabilities):
      raise ValueError("Probabilities should be positive")
      
    return self
      
  def next_num(self):
    return random.choices(self._random_nums, self._probabilities)[0]
```

Questions:

1. Is it allowed to use the `random.choices` method?
2. Do we have constraints regarding the compatibility with older versions of 
   Python?
3. Are we allowed to use external libraries for statistical tests and 
   visualization?

### 5. Get creative and draw the system design

We will implement two classes, one using `random.choices` and the other using
`random.random`. We will provide an abstract class to be used as an interface for
both classes. It will also decouple implementation from client code.

![system_design.png](assets/drawio/system_design.drawio.png)

A sample of the API design is shown below:

```text
# Create a random number generator
rg = (
    RandomGenV1()
    .set_random_nums([-1, 0, 1, 2, 3])
    .set_probabilities([0.01, 0.3, 0.58, 0.1, 0.01])
    .validate_input()
)

# Get a random number
num = rg.next_num()
print("Random number is: ", num)
```

```text
 # Create a hypothesis test
 
 random_numbers = random.
 hypothesis = (
     ChiSquareTest()
     .set_random_numbers()
     .set_probabilities([0.01, 0.3, 0.58, 0.1, 0.01])
     .calc_chi()
     .calc_p()
     .test()
 )
 
 # Hypothesis is True if the distribution is fair
 print("Hypothesis is: ", hypothesis)
```

```text
 # Create a histogram object
 histogram = (
     Histogram()
     .set_random_numbers(random_numbers)
     .build()
     .plot()
 )
 
 # Print the histogram
 print(hist)
```

Typically, at this stage the client shall approve the design, and we can proceed
with the implementation.


### 6. Implement the core

We will implement the following classes:

1. `RandomGenAbc`: An abstract class to be used as an interface.
2. `RandomGenV1`: A class using `random.choices`.
3. `RandomGenV2`: A class using `random.random`.
4. `Histogram`: A helper class that creates a simple histogram object.
5. `ChiSquaredTest`: A helper class to perform the Chi-Squared test.
6. Unit tests for all classes.

### 7. Containerize

We will create a Dockerfile to containerize the solution. We will also create a
`docker-compose.yml` file to run the tests in a container. The application
will consist of a flask server that will implement a simple API to access
the solution. The container will guarantee that the solution will run on any
machine that has Docker installed.


### 8. CI/CD

We will create a GitHub Actions workflow to run the tests on every push to the
main branch. We will also create a GitHub Actions workflow to build and push the
Docker image to Docker Hub on every release.

### 9. Documentation

We will create MkDocs documentation to explain the solution and how to use it.


## Feedback from the client
