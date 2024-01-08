import random
import matplotlib.pyplot as plt
import numpy as np

# Corrected simulation
N = 500  # Number of simulations
sums = []

for _ in range(N):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    sums.append(die1 + die2 + die3)

# Calculating theoretical probabilities
theoretical_probabilities = {}
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            dice_sum = i + j + k
            if dice_sum in theoretical_probabilities:
                theoretical_probabilities[dice_sum] += 1
            else:
                theoretical_probabilities[dice_sum] = 1

# Convert counts to probabilities
for key in theoretical_probabilities:
    theoretical_probabilities[key] /= 6 ** 3

# Plotting the results
plt.figure(figsize=(10, 6))

# Calculating relative frequencies for the simulation
simulated_counts = {i: sums.count(i) / N for i in range(3, 19)}

# Bars for simulated relative frequencies
plt.bar(simulated_counts.keys(), simulated_counts.values(), color="red", alpha=0.5, label='Simulated Relative Frequencies', width=0.4)

# Bars for theoretical probabilities
plt.bar(theoretical_probabilities.keys(), theoretical_probabilities.values(), alpha=0.5, color="blue", label='Theoretical Probabilities', width=0.4)

plt.xlabel('Sum of Dice')
plt.ylabel('Probability')
plt.title('Dice Roll Sum Probabilities: Simulation vs Theoretical')
plt.xticks(np.arange(3, 19))  # Set x-ticks to show every possible sum
plt.legend()
plt.show()
