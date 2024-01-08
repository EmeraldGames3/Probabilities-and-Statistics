import numpy as np
import matplotlib.pyplot as plt

# Define the random variable X and its probabilities
x = [0, 1, 3, 5]
p = [0.4, 0.1, 0.3, 0.2]

# Number of simulations
N = 100

# Use numpy to simulate N random values for X
rng = np.random.default_rng()
simulated_values = rng.choice(x, size=N, replace=True, p=p)

# Create a histogram of the simulated values
plt.hist(simulated_values, bins=np.arange(-0.5, max(x)+1.5, 1), density=True, alpha=0.5, label='Simulated Relative Frequencies')

# Overlay the theoretical probabilities
for value, prob in zip(x, p):
    plt.bar(value, prob, width=0.5, alpha=0.8, color='red', label='Theoretical Probability' if value == x[0] else "")

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Histogram of Simulated vs Theoretical Probabilities for X')
plt.xticks(x)  # Set x-ticks to show each value of X
plt.legend()
plt.show()
