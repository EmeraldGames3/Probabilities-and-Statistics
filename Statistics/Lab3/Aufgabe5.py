import random
from itertools import combinations

# a) Simulation Approach
N = 10000  # Number of simulations
success_count = 0

for _ in range(N):
    birthdays = [random.randint(1, 12) for _ in range(5)]
    birthday_counts = [birthdays.count(month) for month in set(birthdays)]
    if sorted(birthday_counts) == [1, 1, 1, 2]:
        success_count += 1

simulated_probability = success_count / N

# b) Theoretical Probability Calculation
# Choose 2 out of 5 people
choose_two_people = len(list(combinations(range(5), 2)))

# Choose 1 month for these two people, and 3 different months for the remaining
assign_months = 12 * 11 * 10 * 9

# Total possible combinations of birthdays
total_combinations = 12 ** 5

theoretical_probability = (choose_two_people * assign_months) / total_combinations

# Output the results
print(f"Simulated Probability: {simulated_probability}")
print(f"Theoretical Probability: {theoretical_probability}")
