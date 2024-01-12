import math

from numpy import random

n = 1000
x_min = y_min = z_min = -2
x_max = y_max = z_max = 2
target_point = (2, 2, 2)

# a
points = [(random.uniform(x_min, x_max), random.uniform(y_min, y_max),
           random.uniform(z_min, z_max)) for _ in range(n)]
distances = [math.dist(point, target_point) for point in points]
expected_value_x = sum(distances) / n
print("Estimation of the expected value of X: ", expected_value_x)

# b
center = (0, 0, 0)
distances = [math.dist(point, center) for point in points]
inside_points = 0
for distance in distances:
    if distance <= 2:
        inside_points += 1
probability = inside_points / n
print("Probability of a point being inside the sphere: ", probability)

theoretical_probability = (4 / 3 * math.pi * 8) / 64
print("Theoretical probability", theoretical_probability)
