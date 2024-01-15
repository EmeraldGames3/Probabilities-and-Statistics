"""
Die stetige Zufallsgröße X' sei die Durchlaufzeit eines Auftrages und sei gleichmäßig
 verteilt zwischen 10 und 20 Minuten,
d.h. X ~ Unif 10,20.
a) Anband von 2000 Simulationen schätze man folgende Wahrscheinlichkeiten
    a1) die Durchlaufzeit ist zwischen 14 und 18 Minuten P(14 ≤ X ≤ 18)
    a2) die Durchlaufzeit beträgt höchstens 15 Minuten P(X < 15);
    a3) P(A U B), wobei 1= (X <15) und B = (X > 17)
        zwei zufällige Ereignisse sind (A U B entspricht der Vereinigung der beiden Ereignisse)
Für a1), a2) und a3) gebe man die entsprechenden theoretischen Wahrscheinlichkeiten an.
b) Man zeichne cin Histogramm mit 10 Klassen (Balken) für die absoluten Häufigkeiten
 von den 2000 simulierten Werten fur X.
"""
import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

N = 2000
X_uniform = uniform(loc=10, scale=10)  # Unif[10, 20]

# Simulate 2000 values
simulations_uniform = X_uniform.rvs(size=N)

# Estimated probabilities
estimated_probability_uniform_a1 = np.mean((14 <= simulations_uniform) & (simulations_uniform <= 18))
estimated_probability_uniform_a2 = np.mean(simulations_uniform < 15)
estimated_probability_uniform_a3 = np.mean((simulations_uniform < 15) | (simulations_uniform > 17))

# Theoretical probabilities
theoretical_probability_uniform_a1 = X_uniform.cdf(18) - X_uniform.cdf(14)
theoretical_probability_uniform_a2 = X_uniform.cdf(15)
theoretical_probability_uniform_a3 = X_uniform.cdf(15) + (1 - X_uniform.cdf(17))

# Output probabilities
print("Geschätzte Wahrscheinlichkeiten:")
print(f"a1) P(14 ≤ X ≤ 18): {estimated_probability_uniform_a1}")
print(f"a2) P(X < 15): {estimated_probability_uniform_a2}")
print(f"a3) P(A U B): {estimated_probability_uniform_a3}")

print("\nTheoretische Wahrscheinlichkeiten:")
print(f"a1) P(14 ≤ X ≤ 18): {theoretical_probability_uniform_a1}")
print(f"a2) P(X < 15): {theoretical_probability_uniform_a2}")
print(f"a3) P(A U B): {theoretical_probability_uniform_a3}")

# Histogram plotting
number_of_bins = 10
plt.hist(simulations_uniform, bins=number_of_bins, edgecolor='black', density=False)

# Calculate expected frequencies for each bin
expected_frequency_per_bin = N / number_of_bins
plt.hlines(expected_frequency_per_bin, xmin=10, xmax=20, colors='red')

plt.title('Histogram of Simulated Uniform Distribution Values')
plt.xlabel('Durchlaufzeit (Minuten)')
plt.ylabel('Absolute Häufigkeit')
plt.show()
