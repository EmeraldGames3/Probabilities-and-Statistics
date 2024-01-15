import numpy
from random import randrange
from matplotlib.pyplot import bar, show, hist, grid, legend, xticks

N = 200
# 3 Wurfeln
s = [randrange(1, 7) + randrange(1, 7) + randrange(1, 7) for _ in range(N)]
z, count = numpy.unique(s, return_counts=True)
d = dict([(z[i], count[i] / N) for i in range(len(z))])
#TODO - get the key that corresponds to the returned value
max_praktisch = max(d.values())
print(d)
bar(z, count / N, width=0.9, color="red", edgecolor="black", label=" relative Haufigkeiten ", )
print(f'(anhand Simulationen) Man wette auf die Summe {max_praktisch}')
v = []
for i in [1, 2, 3, 4, 5, 6]:
    for j in [1, 2, 3, 4, 5, 6]:
        for k in [1, 2, 3, 4, 5, 6]:
            v.append(i + j + k)

x, count2 = numpy.unique(v, return_counts=True)
max_th = v.__getitem__(max(count2))
m = 6 * 6 * 6
bar(x, count2/m, width=0.7, color="blue", edgecolor="black", label=" theoretische Haufigkeiten", )
legend(loc="lower left")
print(f'(theoretisch) Man wette auf die Summe {max_th}')
xticks(range(3, 19))
grid()
show()

