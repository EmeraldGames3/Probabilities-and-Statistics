import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, expon


N = 1000
X_uniform = uniform(loc=-2, scale=4)  # Unif[-2, 2]
X_exponential = expon(loc=0, scale=2)  # Exp(2)

interval1 = np.linspace(-3, 3, N)
interval2 = np.linspace(0, 4, N)

# dichtefunktionen
pdf_uniform = X_uniform.pdf(interval1)
pdf_exponential = X_exponential.pdf(interval2)

# verteilungsfunktionen
cdf_uniform = X_uniform.cdf(interval1)
cdf_exponential = X_exponential.cdf(interval2)

plt.figure(figsize=(12, 6))

# plot dichtefunktionen
plt.subplot(2, 2, 1)
plt.plot(interval1, pdf_uniform, label='Unif[-2, 2]')
plt.title('Dichtefunktion - Unif[-2, 2]')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(interval2, pdf_exponential, label='Exp(2)')
plt.title('Dichtefunktion - Exp(2)')
plt.legend()

# plot verteilungsfunktionen
plt.subplot(2, 2, 3)
plt.plot(interval1, cdf_uniform, label='Unif[-2, 2]')
plt.title('Verteilungsfunktion - Unif[-2, 2]')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(interval2, cdf_exponential, label='Exp(2)')
plt.title('Verteilungsfunktion - Exp(2)')
plt.legend()

plt.tight_layout()
plt.show()

# b)

simulations_uniform = X_uniform.rvs(size=N)
simulations_exponential = X_exponential.rvs(size=N)

# simulierte Wahrscheinlichkeiten P(1 < X < 1.5)
estimated_probability_uniform = np.mean((1 < simulations_uniform) & (simulations_uniform < 1.5))
estimated_probability_exponential = np.mean((1 < simulations_exponential) & (simulations_exponential < 1.5))

# theoretische Wahrscheinlichkeiten P(1 < X < 1.5)
theoretical_probability_uniform = X_uniform.cdf(1.5) - X_uniform.cdf(1)
theoretical_probability_exponential = X_exponential.cdf(1.5) - X_exponential.cdf(1)

print("Geschätzte Wahrscheinlichkeiten:")
print("Unif[-2, 2]:", estimated_probability_uniform)
print("Exp(2):", estimated_probability_exponential)

print("\nTheoretische Wahrscheinlichkeiten:")
print("Unif[-2, 2]:", theoretical_probability_uniform)
print("Exp(2):", theoretical_probability_exponential)


# c)

mean_uniform = np.mean(simulations_uniform)
variance_uniform = np.var(simulations_uniform)

mean_exponential = np.mean(simulations_exponential)
variance_exponential = np.var(simulations_exponential)

# erwartungswert und varianz theoretisch berechnen
theoretical_mean_uniform = X_uniform.mean()
theoretical_variance_uniform = X_uniform.var()

theoretical_mean_exponential = X_exponential.mean()
theoretical_variance_exponential = X_exponential.var()

print("Geschätzte Werte (Simulationen):")
print("Unif[-2, 2] - Erwartungswert:", mean_uniform)
print("Unif[-2, 2] - Varianz:", variance_uniform)
print("Exp(2) - Erwartungswert:", mean_exponential)
print("Exp(2) - Varianz:", variance_exponential)

print("\nTheoretische Werte:")
print("Unif[-2, 2] - Erwartungswert:", theoretical_mean_uniform)
print("Unif[-2, 2] - Varianz:", theoretical_variance_uniform)
print("Exp(2) - Erwartungswert:", theoretical_mean_exponential)
print("Exp(2) - Varianz:", theoretical_variance_exponential)