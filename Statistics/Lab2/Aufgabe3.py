import numpy as np
import matplotlib.pyplot as plt
import math


def angle_between(v1, v2):
    """Calculate the angle in radians between vectors 'v1' and 'v2'."""
    v1_u = v1 / np.linalg.norm(v1)
    v2_u = v2 / np.linalg.norm(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


def count_obtuse_angles(point, square_corners):
    """Count the number of obtuse angles formed with point A and square corners."""
    obtuse_angles = 0
    for i in range(len(square_corners)):
        v1 = square_corners[i] - point
        v2 = square_corners[(i + 1) % len(square_corners)] - point
        angle = angle_between(v1, v2)
        if angle > np.pi / 2:
            obtuse_angles += 1
    return obtuse_angles


def simulate_and_plot(N, square_corners):
    one_obtuse = []
    two_obtuse = []

    for _ in range(N):
        point = np.random.rand(2)
        obtuse_count = count_obtuse_angles(point, square_corners)

        if obtuse_count == 1:
            one_obtuse.append(point)
        elif obtuse_count == 2:
            two_obtuse.append(point)

    one_obtuse = np.array(one_obtuse)
    two_obtuse = np.array(two_obtuse)

    plt.figure(figsize=(6, 6))
    if len(one_obtuse) > 0:
        plt.scatter(one_obtuse[:, 0], one_obtuse[:, 1], color='blue', label='Exactly 1 Obtuse Angle')
    if len(two_obtuse) > 0:
        plt.scatter(two_obtuse[:, 0], two_obtuse[:, 1], color='red', label='Exactly 2 Obtuse Angles')
    plt.legend()
    plt.title('Random Points with 1 or 2 Obtuse Angles in Square')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.show()

    return len(one_obtuse) / N, len(two_obtuse) / N


# Square corners
square_corners = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

# Number of simulations
N = 10000

# Simulate and plot
prob_one_obtuse, prob_two_obtuse = simulate_and_plot(N, square_corners)
print(f"Probability of Exactly 1 Obtuse Angle: {prob_one_obtuse}")
print(f"Probability of Exactly 2 Obtuse Angles: {prob_two_obtuse}")
