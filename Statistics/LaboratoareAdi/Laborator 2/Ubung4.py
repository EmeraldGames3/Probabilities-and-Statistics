import numpy as np
import matplotlib.pyplot as plt

def is_point_in_upper_triangle(P):
    return P[1] > P[0] and P[1] > 1 - P[0]

def is_point_in_lower_triangle(P):
    return P[1] < P[0] and P[1] < 1 - P[0]

num_points = 500
upper_triangle_count = 0
lower_triangle_count = 0

upper_triangle_points = []
lower_triangle_points = []

for _ in range(num_points):
    P = np.random.rand(2)

    if is_point_in_upper_triangle(P):
        upper_triangle_points.append(P)
        upper_triangle_count += 1
    elif is_point_in_lower_triangle(P):
        lower_triangle_points.append(P)
        lower_triangle_count += 1

probability_upper_triangle = upper_triangle_count / num_points
probability_lower_triangle = lower_triangle_count / num_points

print(f"Probability of a point in the upper triangle: {probability_upper_triangle:.2f}")
print(f"Probability of a point in the lower triangle: {probability_lower_triangle:.2f}")

fig, ax = plt.subplots()

square_vertices = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
square_lines = [[square_vertices[0], square_vertices[1]],
                [square_vertices[1], square_vertices[2]],
                [square_vertices[2], square_vertices[3]],
                [square_vertices[3], square_vertices[0]]]

for line in square_lines:
    ax.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 'k-', linewidth=2)

ax.plot([square_vertices[0][0], square_vertices[2][0]], [square_vertices[0][1], square_vertices[2][1]], 'r-', linewidth=2)
ax.plot([square_vertices[1][0], square_vertices[3][0]], [square_vertices[1][1], square_vertices[3][1]], 'r-', linewidth=2)

if upper_triangle_count > 0:
    upper_triangle_points = np.array(upper_triangle_points)
    ax.scatter(upper_triangle_points[:, 0], upper_triangle_points[:, 1], c='blue', label='Upper Triangle Points')

if lower_triangle_count > 0:
    lower_triangle_points = np.array(lower_triangle_points)
    ax.scatter(lower_triangle_points[:, 0], lower_triangle_points[:, 1], c='green', label='Lower Triangle Points')

ax.set_xlim([-0.1, 1.1])
ax.set_ylim([-0.1, 1.1])
ax.set_aspect('equal', adjustable='box')
plt.title('Simulation')
plt.legend()
plt.show()
