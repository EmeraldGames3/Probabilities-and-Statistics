"""
The independent random variables X and Y have the following probability distribution
    X,Y ~ [(-1,0,1,2) (0.25 0.25 0.25 0.25)]
A) Generate 2000 random data for the random variable X+Y.
 Give the obtained values and the corresponding relative frequencies in,
  for example, print(f"X+Y=... has relative freq. = ...").
B) Draw the histogram of the relative frequencies of the 2000 simulated values for X+Y.
C) Estimate P(X + Y < 1).
D) Give the theoretical probability distribution of X+Y and,
 thus, all possible values X+Y can take and the corresponding
  probabilities, for example, print(f"P(X+Y=...)=...").
E) Give the theoretical value for P(X + Y < 1).
"""
import numpy
import numpy as np
from matplotlib.pyplot import bar, show, grid, legend, xticks

# a)
N = 2000
x = [-1, 0, 1, 2]
P = [0.25, 0.25, 0.25, 0.25, ]

rng = numpy.random.default_rng()
r_x = rng.choice(x, size=N, replace=True, p=P)
r_y = rng.choice(x, size=N, replace=True, p=P)

r = r_x + r_y

# print(r_x)
# print(r_y)
# print(r)

z, count = numpy.unique(r, return_counts=True)
print(f"X+Y= {z} has relative freq. = {count / N}")

bar(z, count / N, width=0.9, color="red", edgecolor="black", label=" relative Haufigkeiten ")

# bar(x, P, width=0.7, color="blue", edgecolor="black", label=" theoretische Wahrscheinlichkeit")
legend(loc="lower left")
xticks(range(-2, 5))
grid()
show()

prob_X_plus_Y_less_than_1 = np.mean(r < 1)
print(f"Estimated P(X + Y < 1) = {prob_X_plus_Y_less_than_1}")

"""
x+y = -2 => -1 + -1
x+y = -1 => -1 + 0 or 0 + -1
x+y = 0 => 0 + 0 or -1 + 1 or 1 + -1
x+y = 1 => 0+1 or 1+0 or 2-1
x+y = 2 => 0+2 or 2+0 or 1+1
x+y = 3 => 1+2 or 2+1
x+y = 4 => 2+2
"""
possible_values = [-2, -1, 0, 1, 2, 3, 4]
theoretical_X_plus_Y = [0.25 * 0.25, 2 * 0.25 * 0.25, 3 * 0.25 * 0.25, 3 * 0.25 * 0.25, 2 * 0.25 * 0.25, 0.25 * 0.25]

print(f"P(X+Y={possible_values}) = {theoretical_X_plus_Y}")

print(f"Theoretischen P(X + Y < 1) = {theoretical_X_plus_Y[0] + theoretical_X_plus_Y[1] + theoretical_X_plus_Y[2]}")
