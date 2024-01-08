import random

# Number of simulations
N = 10000

count_A = 0  # Count of sum being at least 7
count_B_a = 0  # Count of first die being 4 when sum is at least 7 (for part a)
count_B_b = 0  # Count of second die being even when sum is at least 7 (for part b)

# Simulation loop
for _ in range(N):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Condition A: Sum of dice being at least 7
    if die1 + die2 >= 7:
        count_A += 1

        # Condition B for part (a): First die is 4
        if die1 == 4:
            count_B_a += 1

        # Condition B for part (b): Second die is even
        if die2 % 2 == 0:
            count_B_b += 1

# Calculating the simulated conditional probabilities
simulated_prob_a = count_B_a / count_A if count_A > 0 else 0
simulated_prob_b = count_B_b / count_A if count_A > 0 else 0

# Theoretical probabilities
# a) For a given sum >= 7, the first die is 4 in 1 out of 6 possible outcomes (for die 1)
theoretical_prob_a = 1 / 6
# b) The second die being even (2, 4, 6) and resulting in a sum >= 7
# There are 15 total outcomes where the sum is >= 7 (6+1, 5+2, ..., 1+6 twice for symmetry)
# Out of these, 9 outcomes have an even second die (2, 4, 6 in various combinations)
theoretical_prob_b = 9 / 15

# Output the results
print(f"Simulated Conditional Probability for (a): {simulated_prob_a}")
print(f"Theoretical Conditional Probability for (a): {theoretical_prob_a}")
print(f"Simulated Conditional Probability for (b): {simulated_prob_b}")
print(f"Theoretical Conditional Probability for (b): {theoretical_prob_b}")
