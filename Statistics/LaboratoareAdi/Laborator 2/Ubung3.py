import numpy as np
import matplotlib.pyplot as plt

def is_obtuse_triangle(x, y):
    sides = [
        np.linalg.norm(x - y),
        np.linalg.norm(x),
        np.linalg.norm(y)
    ]
    sides.sort()
    return sides[0]**2 + sides[1]**2 < sides[2]**2

num_simulations = 10000
count_obtuse_triangles1 = 0
count_obtuse_triangles2 = 0

for _ in range(num_simulations):
    A = np.random.rand(2)
    square_vertices = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

    obtuse_count = 0
    for vertex in square_vertices:
        if is_obtuse_triangle(A, vertex):
            obtuse_count += 1
    if obtuse_count == 1:
        count_obtuse_triangles1 += 1
    if obtuse_count == 2:
        count_obtuse_triangles2 += 1

probability1 = count_obtuse_triangles1 / num_simulations
probability2 = count_obtuse_triangles2 / num_simulations
print(f"Die Wahrscheinlichkeit, dass genau ein Winkel in A stumpf ist: {probability1:.2f}")
print(f"Die Wahrscheinlichkeit, dass genau zwei Winkeln in A stumpf sind: {probability2:.2f}")


# plotting
fig, ax = plt.subplots()

square_lines = [[square_vertices[0], square_vertices[1]],
                [square_vertices[1], square_vertices[3]],
                [square_vertices[3], square_vertices[2]],
                [square_vertices[2], square_vertices[0]]]

for line in square_lines:
    ax.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 'k-', linewidth=2)

ax.plot(A[0], A[1], 'ro', label='Point A')

for vertex in square_vertices:
    if not np.array_equal(A, vertex):  # exclude diagonal lines
        ax.plot([A[0], vertex[0]], [A[1], vertex[1]], 'b-')

ax.set_xlim([-0.1, 1.1])
ax.set_ylim([-0.1, 1.1])
ax.set_aspect('equal', adjustable='box')
plt.title('Square with Point A and Lines to Vertices')
plt.legend()
plt.show()