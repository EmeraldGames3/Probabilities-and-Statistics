import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

# Definition der Kugeln in der Urne
balls = [0] * 10 + [1] * 20 + [2] * 20

# Anzahl der Simulationen
N = 1000

# Empirische Simulation mit np.prod anstelle von np.product
empirical_X = [np.prod(np.random.choice(balls, size=3, replace=False)) for _ in range(N)]

# Erstellung des Histogramms der empirischen Daten
plt.figure(figsize=(12, 6))
plt.hist(empirical_X, bins=range(min(empirical_X), max(empirical_X) + 2), align='left', color='skyblue', edgecolor='black')
plt.title('Empirisches Histogramm der Werte von X')
plt.xlabel('Wert von X')
plt.ylabel('Absolute Häufigkeit')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Theoretische Analyse mit np.prod
# Alle möglichen Kombinationen von 3 Kugeln ohne Zurücklegen
all_combinations = list(combinations(balls, 3))

# Berechnung des Produkts für jede Kombination mit np.prod
theoretical_product_values = [np.prod(comb) for comb in all_combinations]

# Berechnung der relativen Häufigkeiten der Produktwerte
unique_values, counts = np.unique(theoretical_product_values, return_counts=True)
relative_frequencies = counts / len(theoretical_product_values)

# Theoretisches Histogramm
plt.figure(figsize=(12, 6))
plt.bar(unique_values, relative_frequencies, color='orange', edgecolor='black')
plt.title('Theoretisches Histogramm der Werte von X')
plt.xlabel('Wert von X')
plt.ylabel('Relative Häufigkeit')
plt.xticks(unique_values)
plt.grid(axis='y', alpha=0.75)
plt.show()
