import more_itertools

M = list(more_itertools.distinct_permutations("AABB"))
print(M)
m = len(M)
print("Anzahl Permutationen von AABB mit Wiederholung:", m)
for p in more_itertools.distinct_permutations("1112"):
    print("".join(p))
n = len(list(more_itertools.distinct_permutations("1112")))
print("Anzahl Permutationen von 1112 mit Wiederholung:", n)
