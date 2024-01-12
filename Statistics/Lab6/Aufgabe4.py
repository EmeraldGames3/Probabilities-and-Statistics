import numpy as np
from scipy.stats import uniform

# Anzahl der Simulationen
N = 100000

# Generieren von B und C
B = uniform.rvs(loc=-1, scale=2, size=N)
C = uniform.rvs(loc=-1, scale=2, size=N)

# Diskriminante
D = B ** 2 - 4 * C

# a) Wahrscheinlichkeit, dass beide Wurzeln reell sind (D >= 0)
prob_real_roots = np.mean(D >= 0)

# b) Wahrscheinlichkeit, dass beide Wurzeln positiv sind (D >= 0 und -B/2 > 0 und C < 0)
prob_positive_roots = np.mean((D >= 0) & (-B / 2 > 0) & (C < 0))

# c) Erwartungswert und Varianz der Summe der beiden Wurzeln (-B)
mean_sum_roots = np.mean(-B)
variance_sum_roots = np.var(-B)

# Ergebnisse ausgeben
print(f"a) Wahrscheinlichkeit für reelle Wurzeln: {prob_real_roots:.4f}")
print(f"b) Wahrscheinlichkeit für positive Wurzeln: {prob_positive_roots:.4f}")
print(f"c) Erwartungswert der Summe der Wurzeln: {mean_sum_roots:.4f}")
print(f"   Varianz der Summe der Wurzeln: {variance_sum_roots:.4f}")
