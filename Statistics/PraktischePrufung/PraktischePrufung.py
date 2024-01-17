import itertools

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import bar, show, grid, legend, xticks

N = 2000
M = [0, 1, 2, 3, 4, 5]

results = []
count_exactly_one = 0

for _ in range(N):
    draw = list(np.random.choice(M, size=3, replace=True))
    # print(draw)
    count = 0

    if draw[0] % 2 == 0:
        count += 1

    if draw[1] % 2 == 0:
        count += 1

    if draw[2] % 3 == 0:
        count += 1

    if count == 1:
        count_exactly_one += 1

    results.append(count)

print(f"\nResults for {N} simulations:")
z, count = np.unique(results, return_counts=True)
print(f"{z} = {count}")
print(f"P(X = {z}) = {count / N})")

bar(z, count, width=0.9, color="blue", edgecolor="black", label="absolute Haufigkeit")
show()

bar(z, count / N, width=0.9, color="red", edgecolor="black", label="relative Haufigkeit")
xticks(range(0, 4))
grid()
show()

print()
# c
P_X_gleich_1 = count_exactly_one / N
"""
X = 1
Ziehung = [a ,b ,c]
gerade = [0, 2, 4]
ungerade = [1, 3, 5]

1 a = gerade
    a -> 3
    b -> 3
    c -> 3
2 b = gerade
    a -> 3
    b -> 3
    c -> 3
3 c = gerade
    a -> 3
    b -> 3
    c -> 3
    
P(X = 1) = 3 * (3/6 * 3/6 * 3/6) 
"""
P_X_gleich_1_theoretisch = 3 * ((3 / 6) * (3 / 6) * (3 / 6))

print(f"Simulierten P(X = 1) = {P_X_gleich_1}")
print(f"Theoretischen P(X = 1) = {P_X_gleich_1_theoretisch}")

print()
# d
M = [0, 1, 2, 3]
print(f"Alle variationen gebildet aus 2 Zahlen von {M} sind : {list(itertools.permutations(M, 2))}")
print(f"Anzahl von Variationen aus 2 Zahlen sind: {len(list(itertools.permutations(M, 2)))}")
