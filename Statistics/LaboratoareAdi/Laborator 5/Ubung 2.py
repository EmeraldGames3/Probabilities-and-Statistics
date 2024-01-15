import matplotlib.pyplot as plt
from scipy.stats import expon
import numpy

alpha = 1/12
N = 1000

# a)

data = expon.rvs(loc=0, scale=1/alpha, size=N)
print("die durchsnittliche Druckzeit", numpy.mean(data))   #Erwartungswert anhand simulierten Daten

# b)

plt.hist(data, bins=12, density=True, color="green", edgecolor="black", label="rel. Hfg.")
x=numpy.linspace(min(data), max(data), 80)
y=expon.pdf(x, loc=0, scale=1/alpha)
plt.plot(x, y, "r-", label="Dichtefkt. Exp(1/12)")
plt.legend()
plt.grid()
plt.show()

# c)

# Wahrscheinlichkeiten P(T < 20) = P(T <= 20), P(T > 10), P(10 < T < 30)
print("p1: ", numpy.mean(data<20))
print("theor. w1: ", expon.cdf(20, loc=0, scale=1/alpha))

print("p2: ", numpy.mean(data>10))
print("theor. w2: ", 1-expon.cdf(10, loc=0, scale=1/alpha))

print("p3: ", numpy.mean((data>10) & (data<30)))
print("theor. w3: ", expon.cdf(30, loc=0, scale=1/alpha) - expon.cdf(10, loc=0, scale=1/alpha))

# d)

plt.hist(data, bins=12, density=False, edgecolor="black", label="absolute Hfg.")
plt.legend()
plt.show()
Hfg, Klasse = numpy.histogram(data, bins=12)
for i in range(len(Hfg)):
    print(f'({i+1:2d}) absolute Hfg. {Hfg[i]:3d} in der Klasse [{Klasse[i]:7.4f} , {Klasse[i+1]:7.4f}]')

# e)

t = numpy.linspace(0, 10, 100)
alpha = 1
y = expon.pdf(t, loc=0, scale=1/alpha)
plt.plot(t, y, 'm-', label=f"Dichtefkt. Exp({alpha})")
plt.legend()
plt.grid()
plt.show()
