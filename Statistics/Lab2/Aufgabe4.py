import numpy as np
import matplotlib.pyplot as plt


def is_inside_triangle(p, triangle):
    """Check if point p is inside the triangle."""

    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    d1 = sign(p, triangle[0], triangle[1])
    d2 = sign(p, triangle[1], triangle[2])
    d3 = sign(p, triangle[2], triangle[0])

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    return not (has_neg and has_pos)


def simulate_and_plot_with_triangles_and_square(N):
    # Triangles' vertices
    lower_triangle = np.array([[0, 0], [1, 0], [0.5, 0.5]])
    upper_triangle = np.array([[0, 1], [1, 1], [0.5, 0.5]])

    points = np.random.rand(N, 2)
    inside_triangle = [is_inside_triangle(point, lower_triangle) or is_inside_triangle(point, upper_triangle) for point
                       in points]

    plt.figure(figsize=(6, 6))
    # Points inside triangles
    plt.scatter(points[inside_triangle, 0], points[inside_triangle, 1], color='blue', label='Inside Triangles')
    # Points outside triangles
    plt.scatter(points[~np.array(inside_triangle), 0], points[~np.array(inside_triangle), 1], color='red',
                label='Outside Triangles')

    # Drawing the square boundary
    square = plt.Rectangle((0, 0), 1, 1, fill=False, edgecolor='black', linewidth=1)
    plt.gca().add_patch(square)

    # Drawing the triangles
    plt.plot(*zip(*np.append(lower_triangle, lower_triangle[0:1], axis=0)), color='green', linestyle='dashed')
    plt.plot(*zip(*np.append(upper_triangle, upper_triangle[0:1], axis=0)), color='green', linestyle='dashed')

    plt.title(f'Random Points in Square with Triangles (N = {N})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.axis('equal')
    plt.show()

    probability = sum(inside_triangle) / N
    print(f"Probability of being inside either triangle: {probability}")


# Number of points
N = 5000

# Calculate the probability and plot with triangles and square
simulate_and_plot_with_triangles_and_square(N)
