import numpy as np

x_range = (-1, 1)
y_range = (-1, 1)
z_range = (-1, 1)

num_points = 1000

# generate random points within the specified ranges
random_points_x = np.random.uniform(x_range[0], x_range[1], size=num_points)
random_points_y = np.random.uniform(y_range[0], y_range[1], size=num_points)
random_points_z = np.random.uniform(z_range[0], z_range[1], size=num_points)

distances = np.sqrt(random_points_x**2 + random_points_y**2 + random_points_z**2)

expected_d = np.mean(distances)
variance_d = np.var(distances)

print(f"Erwartungswert von D: {expected_d}")
print(f"Varianz von D: {variance_d}")
