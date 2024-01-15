import numpy as np
import math

# a)

count_sum_above_seven = 0
simulations = 1000

for _ in range(simulations):
    first_roll = 4
    second_roll = np.random.randint(1, 7)

    if first_roll + second_roll >= 7:
        count_sum_above_seven += 1

probability1 = count_sum_above_seven / simulations

# theoretical probability for a)

total_outcomes = 6 ** 2
favorable_outcomes = 0
first_roll = 4

for first_roll in range(1, 7):
    for second_roll in range(1, 7):
        if 4 + second_roll >= 7:
            favorable_outcomes += 1

theoretical_probability1 = favorable_outcomes / total_outcomes

print(f"The probability that the sum is above 7 with the specified conditions is: {probability1:.2f}")

print(f"The theoretical probability that the sum is above 7 with the specified conditions is: {theoretical_probability1:.2f}")

# b)

count_sum_above_seven = 0

for _ in range(simulations):
    first_roll = np.random.randint(1, 7)
    even_numbers = [2, 4, 6]
    second_roll = np.random.choice(even_numbers)

    if first_roll + second_roll >= 7:
        count_sum_above_seven += 1

probability2 = count_sum_above_seven / simulations

# theoretical probability for b)

favorable_outcomes = 0

for first_roll in range(1, 7):
    for second_roll in range(2, 7, 2):
        if first_roll + second_roll >= 7:
            favorable_outcomes += 1

theoretical_probability2 = favorable_outcomes / total_outcomes

print(f"The probability that the sum is above 7 with the specified conditions is: {probability2:.2f}")

print(f"The theoretical probability that the sum is above 7 with the specified conditions is: {theoretical_probability2:.2f}")
