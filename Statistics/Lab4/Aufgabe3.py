from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

# Given parameters
n = 8  # number of trials
p = 0.5  # probability of success on each trial
N = 1000  # number of random values to generate

# Generate random values from the binomial distribution
X = binom.rvs(n, p, size=N)

# Calculate the probability mass function (pmf) for each value of k
k_values = np.arange(0, n+1)
theoretical_probabilities = binom.pmf(k_values, n, p)

# Plot the histogram of the simulated values
plt.hist(X, bins=np.arange(-0.5, n+1.5, 1), density=True, alpha=0.5, label='Simulated Relative Frequencies')

# Overlay the theoretical probabilities
plt.bar(k_values, theoretical_probabilities, width=0.1, alpha=0.8, color='red', label='Theoretical Probability')

# Add labels and title
plt.xlabel('Number of Successes (k)')
plt.ylabel('Probability')
plt.title('Histogram of Binomial Distribution (n=8, p=0.5)')
plt.xticks(k_values)  # Set x-ticks to show each value of k
plt.legend()

# Show the plot
plt.show()

# Calculate the probability of getting exactly k=5 successes
k = 5
probability_k = binom.pmf(k, n, p)
print(f"Man berechnet P(X = {k}) = {probability_k:.6f}")
