import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import geom

# Parameters
p_success = 1/5  # Probability of picking a 5
N = 1000  # Number of simulations

# Simulate the number of trials until the first 5 appears
counts_until_five = []
for _ in range(N):
    count = 0
    while np.random.randint(1, 6) != 5:
        count += 1
    counts_until_five.append(count)

# Convert the list to a numpy array for easier calculations
counts_until_five = np.array(counts_until_five)

# Calculate the probabilities and expected value
probability_X_leq_3 = np.mean(counts_until_five <= 3)
probability_X_gt_3 = np.mean(counts_until_five > 3)
expected_value_X = np.mean(counts_until_five)

# Calculate theoretical probabilities using the geometric distribution
k_values = np.arange(0, max(counts_until_five) + 1)
theoretical_probabilities = geom.pmf(k_values, p_success)

# Plot the histogram of the counts
plt.hist(counts_until_five, bins=np.arange(0.5, max(counts_until_five)+1.5, 1), density=True, alpha=0.7, label='Empirical Histogram')

# Overlay the theoretical probabilities
plt.plot(k_values, theoretical_probabilities, 'ro-', label='Theoretical Probabilities')

# Add labels and title
plt.xlabel('Number of Trials Until First 5')
plt.ylabel('Relative Frequency / Probability')
plt.title('Geometric Distribution of Trials Until First Success')
plt.legend()

# Show the plot
plt.show()

# Print the results
print(f'Probability that X <= 3: {probability_X_leq_3:.4f}')
print(f'Probability that X > 3: {probability_X_gt_3:.4f}')
print(f'Expected Value of X (Simulated): {expected_value_X:.4f}')
print(f'Expected Value of X (Theoretical): {1/p_success - 1:.4f}')  # E(X) for geometric distribution
