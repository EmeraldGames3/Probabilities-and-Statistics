from collections import Counter

import numpy as np
from matplotlib import pyplot as plt
from numpy import mean

# Define the random variable X and its probabilities
x = [0, 1, 2, 3, 4]
p = [0.25, 0.35, 0.25, 0.1, 0.05]

# Number of simulations
N = 100

# Use numpy to simulate N random values for X
rng = np.random.default_rng()
simulated_values = rng.choice(x, size=N, replace=True, p=p)

# Create a histogram of the simulated values
plt.hist(simulated_values, bins=np.arange(-0.5, max(x) + 1.5, 1), density=True, alpha=0.5)
plt.show()

frequency_count = Counter(simulated_values)
print("Wahrscheinlichkeit hochstents 1 Tippfehler", (frequency_count[0] + frequency_count[1]) / N)
print("Simulated Medium Wert", mean(simulated_values))
print("Theoretical Medium Wert", x[0] * p[0] + x[1] * p[1] + x[2] * p[2] + x[3] * p[3] + x[4] * p[4])
