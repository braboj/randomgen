# Plot a custom distribution with the following parameters:
# random_nums = [-1, 0, 1, 2, 3]
# probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

import matplotlib.pyplot as plt
import numpy as np

# Parameters for the custom distribution
random_nums = [-1, 0, 1, 2, 3]

# Generate custom distribution data
data = np.random.choice(random_nums, 10000, p=[0.01, 0.3, 0.58, 0.1, 0.01])

# Plot the histogram
plt.hist(data, bins=len(random_nums), density=True, alpha=0.6, color='b')

# Plot formatting
plt.xlabel('Number')
plt.ylabel('Probability')
plt.title('Custom Distribution')
plt.grid(True)

plt.show()
