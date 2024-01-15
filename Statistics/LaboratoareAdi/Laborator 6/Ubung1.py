import random
import numpy as np
import matplotlib.pyplot as plt

# a), b)

N = 800
X = [4, 5, 6, 7, 8, 9, 10]
P = [0.05, 0.1, 0.1, 0.35, 0.2, 0.1, 0.1]
D = random.choices(X, weights=P, k=N)

erwartungswert = np.mean(D)
print("Erwartungswert anhand Simulationen: ", erwartungswert)


# berechnen theoretische Erwartungswert und Varianz gleichzeitig
s1 = 0
s2 = 0
for i in range(len(X)):
    s1 = s1 + X[i] * P[i]
    s2 = s2 + X[i] * X[i] * P[i]

print("Theoretisches Erwartungswert: ", s1)

varianz = np.var(D)
print("Varianz anhand Simulationen: ", varianz)

print("Theoretisches Varianz: ", s2 - s1 * s1)

c7 = 0
c4 = 0
for x in D:
    if x <= 7:
        c7 += 1
    if x > 4:
        c4 += 1

print("P(X <= 7) anhand Simulationen: ", c7/N)
print("theor. Wkt P(X <= 7): ", sum(np.array(P[:4])))
print("P(X > 4) anhand Simulationen: ", c4/N)
print("theor. Wkt P(X > 4): ", sum(np.array(P[1:])))

# c)

d, c = np.unique(D, return_counts=True)
print(d, c)
plt.bar(d, c/N, width=0.9, color='red', edgecolor='black', label='relative Hfg.')
plt.legend()
plt.show()

plt.bar(d, c, width=0.6, color='green', edgecolor='black', label='absolute Hfg.')
plt.legend()
plt.show()

