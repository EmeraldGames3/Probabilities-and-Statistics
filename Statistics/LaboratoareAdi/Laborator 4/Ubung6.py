import numpy as np
import matplotlib.pyplot as plt

N = 1000
urne = []
urne.extend([1] * 5)
urne.extend([2] * 6)
urne.extend([3] * 9)

def get_two_random_balls():
    chosen_balls = np.random.choice(urne, 2, False)
    return np.sum(chosen_balls)

simulations = [get_two_random_balls() for _ in range(N)]

unique_counts, relative_freq = np.unique(simulations, return_counts=True)
relative_freq = relative_freq / N

plt.bar(unique_counts, relative_freq, align='center')
plt.title(f'Histogram der Summe von zwei zufallig gezogene Kugeln in {N} Experimente')
plt.xlabel('Anzahl der generierten Zahlen')
plt.ylabel('Relative Häufigkeit')
plt.show()

# Erwartungswert

erwartungswert = np.mean(simulations)
print(erwartungswert)