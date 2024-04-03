# Plot a histogram of a binomial distribution with parameters n and p.

import matplotlib.pyplot as plt
import numpy as np

# Parameters for the binomial distribution
n = 10  # number of trials
p = 0.5  # probability of success

# Generate binomial distribution data
data = np.random.binomial(n, p, 10000)

# Plot the histogram
plt.hist(data, bins=10, density=True, alpha=0.6, color='b')

# Plot formatting
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title(f'Binomial Distribution (n = {n}, p = {p})')
plt.grid(True)

plt.show()

