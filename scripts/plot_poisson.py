import matplotlib.pyplot as plt
import numpy as np

# Parameters for the Poisson distribution
lam = 4  # lambda (rate parameter, mean of the distribution)

# Generate Poisson distribution data
data = np.random.poisson(lam, 10000)

# Plot the histogram
plt.hist(data, bins=10, density=True, alpha=0.6, color='b')

# Plot formatting
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.title('Poisson Distribution (lambda = 4)')
plt.grid(True)

plt.show()


