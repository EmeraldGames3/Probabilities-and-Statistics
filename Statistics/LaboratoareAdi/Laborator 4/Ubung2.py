import numpy
from matplotlib.pyplot import bar, show, hist, grid, legend, xticks

# a)
N=10
x=[0, 1, 2, 3, 4]
P=[0.25, 0.35, 0.25, 0.1, 0.05]

rng = numpy.random.default_rng()
r=rng.choice(x, size=N, replace=True, p=P)
print(r)

# b)
count_max_1_fehler = 0
for i in range(len(r)):
    if r[i] == 0 or r[i] == 1:
        count_max_1_fehler += 1

print(f'Wahrscheinlichkeit, dass hoschstens ein Fehler auftaucht ist {count_max_1_fehler/N}')
print(f'Durschnittliche Tippfehlern: {numpy.mean(r)}')
print(f'Theoretische Erwartungswert: {0*0.25 + 1*0.35 + 2*0.25 + 3*0.1 + 4*0.05}')



