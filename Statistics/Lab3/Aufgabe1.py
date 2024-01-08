import random

N = 10000  # Number of simulations

count_A = 0
count_B = 0
count_A_and_B = 0

for _ in range(N):
    # Correct distribution of the balls: 6 red, 4 blue, 6 green
    balls = random.sample(['r'] * 6 + ['b'] * 4 + ['g'] * 6, k=3)

    if 'r' in balls:
        count_A += 1

    if len(set(balls)) == 1:
        count_B += 1

    if len(set(balls)) == 1 and balls[0] == 'r':
        count_A_and_B += 1

P_A = count_A / N
P_B = count_B / N
P_A_and_B = count_A_and_B / N
P_B_given_A = P_A_and_B / P_A

# Theoretical probabilities
total_balls = 6 + 4 + 6  # Total number of balls

# P(A): Probability of drawing at least one red ball
prob_no_red = (10 / total_balls) * (9 / (total_balls - 1)) * (8 / (total_balls - 2))
prob_red = 1 - prob_no_red

# P(B): Probability that all drawn balls are of the same color
prob_same_color = (6 / total_balls) * (5 / (total_balls - 1)) * (4 / (total_balls - 2)) + \
                  (4 / total_balls) * (3 / (total_balls - 1)) * (2 / (total_balls - 2)) + \
                  (6 / total_balls) * (5 / (total_balls - 1)) * (4 / (total_balls - 2))

# P(A ∩ B): Probability of both events happening (drawing three red balls)
prob_red_and_same_color = (6 / total_balls) * (5 / (total_balls - 1)) * (4 / (total_balls - 2))

# P(B|A): Probability of B given A
prob_same_color_given_red = prob_red_and_same_color / prob_red

print("Simulated P_A:", P_A)
print("Theoretical P_A:", prob_red)
print("Simulated P_B:", P_B)
print("Theoretical P_B:", prob_same_color)
print("Simulated P_A_and_B:", P_A_and_B)
print("Theoretical P_A_and_B:", prob_red_and_same_color)
print("Simulated P_B|A:", P_B_given_A)
print("Theoretical P_B|A:", prob_same_color_given_red)
