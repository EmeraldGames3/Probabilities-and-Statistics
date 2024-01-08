from random import randrange

import numpy
from matplotlib.pyplot import bar, show, grid, legend, xticks

N = 1000
daten = [randrange(1, 7) for _ in range(N)]
print(daten)
z, count = numpy.unique(daten, return_counts=True)
d = dict([(z[i], count[i] / N) for i in range(0, 6)])
print(d)
bar(z, count / N, width=0.9, color="red", edgecolor="black", label="relative Haufigkeiten")
D = dict([(k, 1 / 6) for k in range(1, 7)])
bar(D.keys(), D.values(), width=0.7, color="blue", edgecolor="black", label="absolute Haufigkeit")
legend(loc="lower left")
xticks(range(0, 7))
grid()
show()
