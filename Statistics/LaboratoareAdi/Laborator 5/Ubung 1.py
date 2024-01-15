import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy

# a)

mu = 199
sigma = 3
N = 1000
Daten = norm.rvs(mu, sigma, N)   # generierte Werte fur ZG : X ~ N(mu, sigma^2)
# print(Daten)
m = numpy.mean(Daten)      # im Mittel / Erwartungswert
print("abgefullte Menge Tee - im Mittel ", m)

# b)
# um zu erhalten wie viele Packungen unter 195g enthalten

print("p1 Daten <= 195: ", sum(Daten < 195) / N)   # um Wahrscheinlichkeit zu erhalten
print("p1 Daten <= 195: ", numpy.mean(Daten <= 195))
print("w1 theoretische Wharscheinlichkeit P(X <= 195): ", norm.cdf(195, mu, sigma))
print("p2 195 <= Daten <= 198: ", numpy.mean((Daten >= 195) & (Daten <= 198)))
print("w2 theoretische Wharscheinlichkeit P(195 <= X <= 198): ", norm.cdf(198, mu, sigma) - norm.cdf(195, mu, sigma))
print("p3 Daten >= 195: ", numpy.mean(Daten >= 195))
print("w3 theoretische Wharscheinlichkeit P(X > 195): ", 1 - norm.cdf(195, mu, sigma))

# c)

Hfg, Klasse = numpy.histogram(Daten, bins=16)
print("Haufigkeit in jeder Klasse (in jedem Intervall): ", Hfg)
print("Lange Hfg: ", len(Hfg))
print("Klassenenden (Endpunkte der Intervalle): ", Klasse)
print("Lange Klasse: ", len(Klasse))

for i in range(len(Hfg)):
    print(f'({i+1:2d}) absolute Hfg. {Hfg[i]:3d} in der Klasse [{Klasse[i]:7.4f} , {Klasse[i+1]:7.4f}]')


plt.hist(Daten, bins=16, density=True, edgecolor='black', label='rel. Hfg.')
x = numpy.linspace(min(Daten), max(Daten), 100)
y = norm.pdf(x, mu, sigma)
plt.plot(x, y, 'r')
plt.legend()
plt.grid()
plt.show()
