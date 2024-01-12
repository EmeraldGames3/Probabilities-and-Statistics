import random
import numpy as np

n = 1000
X = [4, 5, 6, 7, 8, 9, 10]
P = [0.05, 0.1, 0.1, 0.35, 0.2, 0.1, 0.1]

D = random.choices(X, weights=P, k=n)

# Calculate the expected value
expected_value = np.mean(D)
print("Expected value E(X):", expected_value)

# Theoretical Expected value E(X)
expected_value = sum(x * p for x, p in zip(X, P))
print("Theoretical Expected value E(X):", expected_value)

# Calculate the variance
variance = np.var(D)
print("Variance V(X):", variance)

# Theoretical Variance V(X)
expected_value_squared = sum(x**2 * p for x, p in zip(X, P))
variance = expected_value_squared - expected_value**2
print("Theoretical Variance V(X):", variance)

# Calculate the probability P(X ≤ 7)
prob_x_leq_7 = sum(1 for d in D if d <= 7) / n
print("P(X ≤ 7):", prob_x_leq_7)

# Theoretical Probability P(X ≤ 7)
prob_x_leq_7 = sum(p for x, p in zip(X, P) if x <= 7)
print("Theoretical P(X ≤ 7):", prob_x_leq_7)

# Calculate the probability P(X > 4)
prob_x_gt_4 = sum(1 for d in D if d > 4) / n
print("P(X > 4):", prob_x_gt_4)

# Theoretical Probability P(X > 4)
prob_x_gt_4 = sum(p for x, p in zip(X, P) if x > 4)
print("Theoretical P(X > 4):", prob_x_gt_4)

import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
plt.hist(D, bins=len(X), density=True, edgecolor='black')
plt.title('Relativen Häufigkeiten')
plt.xlabel('Werte')
plt.ylabel('Relative Häufigkeit')

# Absolute Häufigkeiten
plt.subplot(1, 2, 2)
plt.hist(D, bins=len(X), density=False, edgecolor='black', color='r')
plt.title('Absoluten Häufigkeiten')
plt.xlabel('Werte')
plt.ylabel('Absolute Häufigkeit')

plt.tight_layout()
plt.show()