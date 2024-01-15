import random
from random import sample
import math
from math import factorial, perm, comb
import itertools
from itertools import permutations, combinations

# a) erstelle eine Liste mit den Permutationen von ABC

letters = "ABC"
print(*permutations(letters))

# b) gesamte Anzahl von Permutationen

print(perm(len(letters)))

# c) man generiere eine zufallige Permutation von MATHE

mathe = "MATHE"
random.sample = sample(mathe, len(mathe))
print(random.sample)

# d) man generiere eine zufallige Permutation von MATHE gebildet aus 3 Buchstaben

mathe = "MATHE"
random.sample = sample(mathe, 3)
print(random.sample)

# e) man generiere alle Variationen von MATHE gebildet aus 3 Buchstaben

print(*permutations(mathe, 3))

# f) man generiere die Anzahl der Variationen von ABC mit 3 Buchstaben

print(perm(len(mathe), 3))

# g) man generiere alle Kombinationen mit 3 Buchstaben aus MATHE

print(*combinations(mathe, 3))

# h) man generiere die Anzahl der Kombinationen mit 3 Buchstaben aus MATHE

print(comb(len(mathe), 3))