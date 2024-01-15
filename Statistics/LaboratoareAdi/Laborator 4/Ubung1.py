import numpy
from matplotlib.pyplot import bar, show, hist, grid, legend, xticks

N=1000
x=[0 ,1 ,3 ,5]
P=[0.4 ,0.1 ,0.3 ,0.2]
rng = numpy.random.default_rng()
r=rng.choice(x, size=N , replace=True, p=P)

z, count = numpy.unique(r, return_counts=True)

bar(z, count / N, width=0.9, color="red", edgecolor="black", label=" relative Haufigkeiten ")

bar(x, P, width=0.7, color="blue", edgecolor="black", label=" theoretische Wahrscheinlichkeit")
legend(loc="lower left")
xticks(range(-1, 6))
grid()
show()

