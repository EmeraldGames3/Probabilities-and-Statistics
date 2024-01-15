import numpy as np
import math

N = 1000
white_balls = 4
black_balls = 6
total_balls = 10

# theoretical probability for each black ball picked

p_white_ball = 4 / 10
p_black_ball = 6 / 10
p_1black_1white = 6 / 10 * 4 / 9
p_2black_1white = 6 / 10 * 5 / 9 * 4 / 8
p_3black = 6 / 10 * 5 / 9 * 4 / 8

print(f"theoretische Wahrscheinlichkeit fur keinen schwarzen Kugel gezogen: {p_white_ball}")
print(f"theoretische Wahrscheinlichkeit fur einen schwarzen Kugel gezogen: {p_1black_1white}")
print(f"theoretische Wahrscheinlichkeit fur zwei schwarze Kugeln gezogen: {p_2black_1white}")
print(f"theoretische Wahrscheinlichkeit fur drei schwarzen Kugeln gezogen: {p_3black}")

urne = []
urne.extend(['w'] * white_balls)
urne.extend(['b'] * black_balls)


def random_values_simulation():
    count_black = 0
    random_choice = np.random.choice(urne, size=3, replace=False)
    for element in random_choice:
        if element == 'w' or count_black == 3:
            break
        else:
            count_black += 1
    return count_black


def given_points():
    assigned_points = 0
    counts = random_values_simulation()
    if counts == 3:
        assigned_points += 30
    elif counts == 2:
        assigned_points += 25
    else:
        assigned_points -= 5
    return assigned_points


simulated_scenario = [given_points() for _ in range(N)]
avg_points = np.mean(simulated_scenario)
print(f"Average points obtained during simulated scenario: {avg_points}")

# theoretische Wahrscheinlichkeiten

p_negative_points = p_white_ball + p_1black_1white
p_25_points = p_2black_1white
p_30_points = p_3black

print(f"theoretical probability of obtaining negative points: {p_negative_points}")
print(f"theoretical probability of obtaining 25 points: {p_25_points}")
print(f"theoretical probability of obtaining 30 points: {p_30_points}")
