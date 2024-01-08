import math
import random
import numpy as np
from matplotlib.pyplot import axis, plot, figure, show

num_points = 1000
points_x_inside_circle = []
points_y_inside_circle = []
points_x_outside_circle = []
points_y_outside_circle = []

points_inside_circle = 0

for _ in range(num_points):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    distance = np.sqrt((x - 0.5)**2 + (y - 0.5)**2)  # Distance from center (0.5, 0.5)
    if distance <= 0.5:
        points_x_inside_circle.append(x)
        points_y_inside_circle.append(y)
        points_inside_circle += 1
    else:
        points_x_outside_circle.append(x)
        points_y_outside_circle.append(y)

probability_inside_circle = points_inside_circle / num_points
estimated_pi = 4 * probability_inside_circle

print(f"Estimated Probability inside circle: {probability_inside_circle:.4f}")
print(f"Theoretical Probability (π/4): {math.pi / 4:.4f}")
print(f"Estimated Pi: {estimated_pi:.4f}")
print(f"Theoretical Pi: {math.pi}")

fig = figure()
axis("square")
axis((0, 1, 0, 1))
plot(points_x_inside_circle, points_y_inside_circle, "ro", label="Inside Circle")
plot(points_x_outside_circle, points_y_outside_circle, "bo", label="Outside Circle")
fig.suptitle("Points Inside and Outside the Circle", fontweight="bold")
show()
