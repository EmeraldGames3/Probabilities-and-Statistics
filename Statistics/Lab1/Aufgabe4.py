import itertools
from itertools import combinations_with_replacement
print("Alle Kombinationen von ABC je 2, mit Wiederholung")

M = list(combinations_with_replacement("ABC", 2))
k = len(M)

print(M)
print("Anzahl Kombinationen von ABC je 2 mit Wiederholung:",k)
