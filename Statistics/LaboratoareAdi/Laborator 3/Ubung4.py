import random
import numpy as np

c1, c2, a1, a2 = 0, 0, 0, 0
N = 10000

A = list(range(1, 21))

for _ in range (N):
    i = np.random.randint(len(A))                           # random number between 1 and 20
    v = A[i]                                                # v takes the value of the i-th position in list A
    c1 = c1 + (v % 2)                                       # c1 is incremented if the value of the element on position A[i] is odd
    c2 = c2 + ((v % 2) == 0)                                # c2 is incremented if the value of the element on position A[i] is even
    a1 = a1 + (v % 2) + ((v % 3) == 0)                      # a1 is incremented by either 0, 1 or 2, depending on the conditions evaluated (odd and divisible by 3)
    a2 = a2 + ((v % 2) == 0) * (6 <= v <= 10)               # a2 is incremented either by 0, 6, 8 or 10, depending on the conditions evaluated (even and between 6 and 10)

p1 = a1 / c1                                                # probability of getting a number that is odd or divisible by 3
p2 = a2 / c2                                                # probability of getting an even number between 6 and 10
p3 = c1 / N                                                 # probability of getting an odd number

print("Aus den Simulationen:")
print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p3 = {p3}")

theoretical_p1 = (len([v for v in A if v % 2 == 1 or v % 3 == 0]) / len(A))
theoretical_p2 = (len([v for v in A if 6 <= v <= 10 and v % 2 == 0]) / len([v for v in A if v % 2 == 0]))
theoretical_p3 = (len([v for v in A if v % 2 == 1]) / len(A))

print("Theoretische Wahrschenlichkeiten:")
print(f"theor. p1: {theoretical_p1}")
print(f"theor. p2: {theoretical_p2}")
print(f"theor. p3: {theoretical_p3}")