# Theoretical Probability Distribution of X
# X is the number of black balls drawn

# Total number of balls
total_balls = 10
# Number of black balls
black_balls = 6
# Number of white balls
white_balls = 4

# Probabilities of drawing 0, 1, 2, or 3 black balls before drawing a white ball or before drawing 3 balls
P_X = {
    0: white_balls / total_balls,
    1: (black_balls / total_balls) * (white_balls / (total_balls - 1)),
    2: (black_balls / total_balls) * ((black_balls - 1) / (total_balls - 1)) * (white_balls / (total_balls - 2)),
    3: (black_balls / total_balls) * ((black_balls - 1) / (total_balls - 1)) * ((black_balls - 2) / (total_balls - 2))
}

# Adjust P_X[2] to account for the white ball being drawn as the third ball
P_X[2] = P_X[2] * (white_balls / (total_balls - 2))

# Output the theoretical probabilities
for x, p in P_X.items():
    print(f"P(X = {x}) = {p:.4f}")

# Theoretical Probability Distribution of Y
# Y is the points scored by the player
# Points for different outcomes
points = {0: -5, 1: -5, 2: 25, 3: 30}

# Calculate probabilities for Y outcomes
P_Y = {
    30: P_X[3],  # Probability of drawing three black balls
    25: P_X[2],  # Probability of drawing two black balls and then a white ball
    -5: P_X[0] + P_X[1]  # Probability of drawing a white ball first or one black ball then a white
}

# Output the probabilities for Y outcomes
for points, probability in P_Y.items():
    print(f"P(Y = {points}) = {probability:.4f}")

# Expected value calculation
E_Y = sum(P_Y[points] * points for points in P_Y)

# Output the theoretical expected value
print(f"The theoretical expected value of Y is E(Y) = {E_Y:.2f} points")
