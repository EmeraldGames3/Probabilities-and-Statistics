import itertools

l = [1, 2, 3, 4]  # Kartons
kugeln = 6

print(list(itertools.combinations_with_replacement(l, kugeln)))
n = len(list(itertools.combinations_with_replacement(l, kugeln)))
print(n)
