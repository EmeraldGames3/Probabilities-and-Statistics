import itertools
import math
import random

# a
s = "ABC"
print(list(itertools.permutations(s)))

# b
print(math.perm(len(s)))

# c
s = "MATHE"
print(random.sample(s, len(s)))

# d
print(random.sample(s, 3))

# e
print(list(itertools.permutations(s, 3)))

# f
print(math.perm(len(s), 3))

# g
print(list(itertools.combinations(s, 3)))

# h
print(math.comb(len(s), 3))
