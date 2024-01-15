import math

from scipy.stats import uniform
import numpy as np
import sympy as sp

x = sp.symbols('x')

min_b, max_b = -1, 1
min_c, max_c = -1, 1

b = uniform(loc=min_b, scale=max_b - min_b).rvs()
c = uniform(loc=min_c, scale=max_c - min_c).rvs()

equation = sp.Eq(x**2 + b*x + c, 0)

print("Second-degree equation:", equation)

delta = b ** 2 - 4 * c

prob_real_solutions = np.mean(delta >= 0)

print(f"The probability that the two solutions are real is: {prob_real_solutions}")

solution1 = (-b + np.sqrt(delta)) / 2
solution2 = (-b - np.sqrt(delta)) / 2

positive_root_conditions = (delta >= 0) & (solution1 > 0) & (solution2 > 0)   # when error encountered => complex sol
prob_positive_solutions = np.mean(positive_root_conditions)

print(f"The probability that the two solutions are positive is: {prob_positive_solutions}")

erwartungswert1 = np.mean(solution1)
erwartungswert2 = np.mean(solution2)
varianz1 = np.var(solution1)
varianz2 = np.var(solution2)

print(f"Erwartungswert fur Solution 1: {erwartungswert1}")
print(f"Erwartungswert fur Solution 2: {erwartungswert2}")
print(f"Varianz fur Solution 1: {varianz1}")
print(f"Varianz fur Solution 2: {varianz2}")
