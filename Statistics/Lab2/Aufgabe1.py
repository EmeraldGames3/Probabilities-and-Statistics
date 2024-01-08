import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import axis,plot,figure,show,legend
from math import dist

# a)
num_simulations = 100000

k = 23

n = 365

event_count = 0

for _ in range(num_simulations):
    birthdays = np.random.randint(1, n + 1, size=k)

    if len(birthdays) != len(set(birthdays)):
        event_count += 1

simulated_prob = event_count / num_simulations
print(f"Simulated probability: {simulated_prob:.4f}")


# b)
def theoretical_probability(k, n):
    p = 1.0
    for i in range(1, k):
        p *= (n - i) / n
    return 1 - p


theoretical_prob = theoretical_probability(k, n)
print(f"Theoretical probability: {theoretical_prob:.4f}")