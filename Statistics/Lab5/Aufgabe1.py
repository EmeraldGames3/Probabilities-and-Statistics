import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Part (a) - Simulate Data
mu = 199
sigma = 3
N = 1000
Daten = norm.rvs(mu, sigma, N)

# Average filled amount
average_amount = np.mean(Daten)
print("Average filled amount:", average_amount, "g")

# Part (b) - Probability Calculations
probability_less_195 = norm.cdf(195, mu, sigma)
probability_between_195_198 = norm.cdf(198, mu, sigma) - norm.cdf(195, mu, sigma)
probability_more_195 = 1 - norm.cdf(195, mu, sigma)

print("Probability of less than 195g:", probability_less_195)
print("Probability between 195g and 198g:", probability_between_195_198)
print("Probability of more than 195g:", probability_more_195)

# Part (c) - Histogram and Density Function
plt.hist(Daten, bins=16, density=True, edgecolor="black", label="Relative Frequency")
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
plt.plot(x, norm.pdf(x, mu, sigma), label="Density Function")
plt.xlabel('Tea Weight in g')
plt.ylabel('Probability')
plt.title('Histogram and Density Function of Tea Weight')
plt.legend()
plt.show()

# Part (d) - Absolute Frequencies in Classes
counts, bins = np.histogram(Daten, bins=16)
for i in range(len(counts)):
    print(f"Klasse {i + 1}: {counts[i]} Daten, [{bins[i]}, {bins[i + 1]}]")
