import math

import numpy as np
import math
from scipy.stats import uniform

# a)

N = 1000
x = uniform.rvs(loc=-2, scale=4, size=N)  # loc + scale = Endwert, also 2, weil Intervall zwischen -2, 2 ist
y = uniform.rvs(loc=-2, scale=4, size=N)
z = uniform.rvs(loc=-2, scale=4, size=N)

X = [math.dist([x[i], y[i], z[i]], [2, 2, 2]) for i in range(len(x))]
XX = [((x[i] - 2) ** 2 + (y[i] - 2) ** 2 + (z[i] - 2) ** 2) ** 0.5 for i in range(len(x))]  # equivalente mathematische Formel

# b)

Z = [math.dist([x[i], y[i], z[i]], [0, 0, 0]) for i in range(len(x))]
R = 2  # Radius Kugel
L = 4  # Lange einer Kante im Quader
c = 0

for z in Z:
      if z <= R:
            c += 1

print("Wkt. zufalliger Punkt im Inneren der Kugel anhand Simulationen: ", c/len(Z))
print("Theor. Wkt. zufalliger Punkt im Inneren der Kugel: ", ((4/3) * math.pi * (R**3))/(L**3))
