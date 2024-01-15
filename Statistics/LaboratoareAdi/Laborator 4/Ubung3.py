import scipy
import numpy
from matplotlib.pyplot import bar, show, hist, grid, legend, xticks

N = 1000
n = 8
p = 0.5
vector = []

for i in range(n + 1):
    vector.append(i)

X = scipy.stats.binom.rvs(n, p, size=N)
w = scipy.stats.binom.pmf(vector, n, p)

xx, count = numpy.unique(X, return_counts=True)
bar(xx, count/N, width=0.6, color="blue", edgecolor="black", label="relative Haufigkeiten ")

bar(vector, w, width=0.9, color="red", edgecolor="black", label="theoretische Haufigkeiten ")
xticks(range(0, n + 1))
legend(loc="upper right")

grid()
show()

