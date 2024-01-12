import numpy as np
from scipy.special import comb

def simulate_game():
    # Urn contains 3 blue (b), 3 red (r), and 4 white (w) balls
    urn = ['b'] * 3 + ['r'] * 3 + ['w'] * 4
    drawn_balls = np.random.choice(urn, size=3, replace=False)
    unique_colors = len(set(drawn_balls))

    # Payoff conditions
    if unique_colors == 1:
        return 5  # All balls have the same color
    elif unique_colors == 3:
        return 2  # All balls have different colors
    else:
        return -1  # Other cases

# Number of simulations
N = 10000

# Run simulations
simulated_results = [simulate_game() for _ in range(N)]
average_gain_loss_simulation = np.mean(simulated_results)

# Theoretical expected value calculation
total_ways = comb(10, 3)
# Probability and payoff for each outcome
prob_same_color = (comb(3, 3) + comb(3, 3) + comb(4, 3)) / total_ways
prob_diff_color = (comb(3, 1) * comb(3, 1) * comb(4, 1)) / total_ways
expected_value_theoretical = prob_same_color * 5 + prob_diff_color * 2 + (1 - prob_same_color - prob_diff_color) * -1

# Output results
print(f"Average Gain/Loss per Game (Simulation): {average_gain_loss_simulation:.2f} euros")
print(f"Theoretical Expected Value: {expected_value_theoretical:.2f} euros")
