import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, expon

# Plotting the PDF and CDF for the Uniform and Exponential Distributions
# a) Uniform Distribution Unif[-2, 2]
x_unif = np.linspace(-3, 3, 1000)
pdf_unif = uniform.pdf(x_unif, loc=-2, scale=4)  # scale is width (b - a)
cdf_unif = uniform.cdf(x_unif, loc=-2, scale=4)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x_unif, pdf_unif, label='PDF of Unif[-2, 2]')
plt.plot(x_unif, cdf_unif, label='CDF of Unif[-2, 2]')
plt.title('Uniform Distribution Unif[-2, 2]')
plt.xlabel('x')
plt.ylabel('Probability')
plt.legend()

# b) Exponential Distribution Exp(2)
x_exp = np.linspace(0, 4, 1000)
pdf_exp = expon.pdf(x_exp, scale=1/2)  # scale is 1/lambda
cdf_exp = expon.cdf(x_exp, scale=1/2)

plt.subplot(1, 2, 2)
plt.plot(x_exp, pdf_exp, label='PDF of Exp(2)')
plt.plot(x_exp, cdf_exp, label='CDF of Exp(2)')
plt.title('Exponential Distribution Exp(2)')
plt.xlabel('x')
plt.ylabel('Probability')
plt.legend()

plt.tight_layout()
plt.show()

# Simulating and Comparing Probabilities, Expectations, and Variances
N = 10000  # Number of simulations

# Simulate values for both distributions
simulated_unif = uniform.rvs(loc=-2, scale=4, size=N)  # Unif[-2, 2]
simulated_exp = expon.rvs(scale=1/2, size=N)           # Exp(2)

# Estimate P(1 < X < 1.5) for both distributions
prob_unif = np.mean((1 < simulated_unif) & (simulated_unif < 1.5))
prob_exp = np.mean((1 < simulated_exp) & (simulated_exp < 1.5))

# Theoretical probabilities
theoretical_prob_unif = uniform.cdf(1.5, loc=-2, scale=4) - uniform.cdf(1, loc=-2, scale=4)
theoretical_prob_exp = expon.cdf(1.5, scale=1/2) - expon.cdf(1, scale=1/2)

# Estimate E(X) and V(X) for both distributions
mean_unif = np.mean(simulated_unif)
var_unif = np.var(simulated_unif)

mean_exp = np.mean(simulated_exp)
var_exp = np.var(simulated_exp)

# Output results
print("Uniform Distribution Unif[-2, 2]:")
print(f"Simulated P(1 < X < 1.5): {prob_unif:.4f}, Theoretical P(1 < X < 1.5): {theoretical_prob_unif:.4f}")
print(f"Simulated E(X): {mean_unif:.4f}, Simulated V(X): {var_unif:.4f}\n")

print("Exponential Distribution Exp(2):")
print(f"Simulated P(1 < X < 1.5): {prob_exp:.4f}, Theoretical P(1 < X < 1.5): {theoretical_prob_exp:.4f}")
print(f"Simulated E(X): {mean_exp:.4f}, Simulated V(X): {var_exp:.4f}")
