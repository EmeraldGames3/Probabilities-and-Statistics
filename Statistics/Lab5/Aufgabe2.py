import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Part (a) - Simulate Data and Mean Calculation
alpha = 1 / 12
N = 1000
Daten = stats.expon.rvs(loc=0, scale=1 / alpha, size=N)
mean = np.mean(Daten)
print("Mean print time:", mean, "seconds")

# Part (b) - Histogram and Class Frequencies
Hfg, Klassen = np.histogram(Daten, bins=12)
for i in range(len(Hfg)):
    print(f"Klasse {i + 1}: {Hfg[i]} Daten, [{Klassen[i]}, {Klassen[i + 1]}]")

# Part (c) - Probability Estimates
prob_less_than_20 = stats.expon.cdf(20, loc=0, scale=1 / alpha)
prob_greater_than_10 = 1 - stats.expon.cdf(10, loc=0, scale=1 / alpha)
prob_between_10_and_30 = stats.expon.cdf(30, loc=0, scale=1 / alpha) - stats.expon.cdf(10, loc=0, scale=1 / alpha)

print("P(T < 20):", prob_less_than_20)
print("P(T > 10):", prob_greater_than_10)
print("P(10 < T < 30):", prob_between_10_and_30)

# Part (d) - Histogram with Relative Frequencies and Density Function
plt.hist(Daten, bins=12, density=True, edgecolor="black", label="Relative Frequencies")
x = np.linspace(min(Daten), max(Daten) + 2, 100)
y = stats.expon.pdf(x, loc=0, scale=1 / alpha)
plt.plot(x, y, 'r-', label="Density Function")
plt.xlabel('Time (seconds)')
plt.ylabel('Density')
plt.title('Histogram and Density Function of Print Times')
plt.legend()
plt.show()

# Part (e) - Histogram with Absolute Frequencies
plt.hist(Daten, bins=12, density=False, edgecolor="black", label="Absolute Frequencies")
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Histogram of Print Times with Absolute Frequencies')
plt.legend()
plt.show()

# Part (f) - Density Function of Exp(1) on [0, 10]
x2 = np.linspace(0, 10, 100)
y2 = stats.expon.pdf(x2, loc=0, scale=1)
plt.plot(x2, y2, 'g', label="Density Function Exp(1)")
plt.xlabel('Time (seconds)')
plt.ylabel('Density')
plt.title('Density Function of Exp(1) on [0, 10]')
plt.legend()
plt.show()
