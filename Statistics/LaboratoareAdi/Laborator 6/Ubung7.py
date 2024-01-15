import math
import random

b = 3
r = 3
w = 4
alle = b + r + w
z = 3  # ohne Zurucklegen; 3 -> alle Kugeln dieselbe Farbe haben; 2 -> alle Kugeln verschiedene Farben; -1 -> sonst

Liste = ["b"] * b + ["r"] * r + ["w"] * w
print(Liste)

t = 0
N = 1000
for _ in range(N):
    R = random.sample(Liste, z)  # Ziehen ohne Zurucklegen
    if len(set(R)) == 1:  # alle Kugeln haben dieselbe Farbe
        t += 5
    elif len(set(R)) == 3:
        t += 2
    else:
        t -= 1

print("Gewinn oder Verlust im Mittel: ", t / N)  # simulierter Erwartungswert fur Gewinn oder Verlust
s = 0
X = [5, 2, -1]  # Gewinn oder Verlust in Euro
p1 = (b / alle) * ((b - 1) / (alle - 1)) * ((b - 2) / (alle - 2)) + (r / alle) * ((r - 1) / (alle - 1)) * (
            (r - 2) / (alle - 2)) + (w / alle) * ((w - 1) / (alle - 1)) * ((w - 2) / (alle - 2))
p2 = math.factorial(3) * (b / alle) * (r / (alle - 1)) * (w / (alle - 2))
p3 = 1 - p1 - p2
print(p1, p2, p3)
P = [p1, p2, p3]  # die Wahrscheinlichkeit von X
for i in range(len(X)):
    s = s + X[i] * P[i]
print("theor. Erwartungswert fur Gewinn oder Verlust: ", s)
