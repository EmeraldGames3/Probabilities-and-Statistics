from itertools import combinations
import numpy as np
import matplotlib.pyplot as plt

# Define the balls in the urn
urn = [1] * 5 + [2] * 6 + [3] * 9

# Calculate all possible unique combinations of two balls
unique_combinations = list(combinations(urn, 2))

# Calculate all possible sums and their counts
sums_counts = {}
for combo in unique_combinations:
    combo_sum = sum(combo)
    if combo_sum in sums_counts:
        sums_counts[combo_sum] += 1
    else:
        sums_counts[combo_sum] = 1

# Calculate theoretical probabilities
theoretical_probs = {k: v / len(unique_combinations) for k, v in sums_counts.items()}
theoretical_sums, theoretical_freqs = zip(*theoretical_probs.items())

# Theoretical expected value
theoretical_expected_value = sum(k * v for k, v in theoretical_probs.items())

# Number of simulations
N = 1000

# Simulate the drawing of 2 balls without replacement N times and calculate the sum
simulated_sums = [sum(np.random.choice(urn, size=2, replace=False)) for _ in range(N)]

# Plot the histogram of the simulated sums
plt.hist(simulated_sums, bins=range(min(simulated_sums), max(simulated_sums)+2), density=True, alpha=0.5, label='Simulated Relative Frequencies')

# Overlay the theoretical probabilities
plt.bar(theoretical_sums, theoretical_freqs, width=0.1, alpha=0.8, color='red', label='Theoretical Probability')

# Add labels and title
plt.xlabel('Sum of Balls')
plt.ylabel('Relative Frequency / Probability')
plt.title('Histogram of Sums from Drawing 2 Balls Without Replacement')
plt.legend()

# Show the plot
plt.show()

# Estimated expected value from the simulation
empirical_expected_value = np.mean(simulated_sums)

# Print the estimated and theoretical expected values
print(f"Estimated Expected Value of X (Simulated): {empirical_expected_value:.4f}")
print(f"Theoretical Expected Value of X: {theoretical_expected_value:.4f}")
