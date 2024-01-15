import numpy as np
import matplotlib.pyplot as plt
N = 10000

# a)
def simulate_experiment():
    numbers = []
    while True:
        numbers.append(np.random.randint(1, 6))
        if numbers[-1] == 5:
            break
    return len(numbers)

counts = np.array([simulate_experiment() for _ in range(N)])

unique_counts, relative_frequencies = np.unique(counts, return_counts=True)
relative_frequencies = relative_frequencies / N

plt.bar(unique_counts, relative_frequencies, align='center')
plt.title(f'Histogram der Anzahl der generierten Zahlen vor der ersten 5 ({N} Experimente)')
plt.xlabel('Anzahl der generierten Zahlen')
plt.ylabel('Relative Häufigkeit')
plt.show()

# b)

c3 = 0

for _ in range(N):
    x = simulate_experiment()
    if x <= 3:
        c3 += 1

simulated_probability1 = c3 / N
print(simulated_probability1)

c3 = 0

for _ in range(N):
    x = simulate_experiment()
    if x > 3:
        c3 += 1

simulated_probability2 = c3 / N
print(simulated_probability2)

# Erwartungswert

counts = np.array([simulate_experiment() for _ in range(N)])
erwartungswert = np.mean(counts)
print(erwartungswert)