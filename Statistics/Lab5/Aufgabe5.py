import numpy as np
from scipy.stats import uniform
from scipy.integrate import tplquad

# Define the limits of the cube
a, b = -1, 1

# The integrand function: sqrt(x^2 + y^2 + z^2)
def integrand(z, y, x):
    return np.sqrt(x**2 + y**2 + z**2)

# Calculate the theoretical expected distance (mean)
theoretical_mean, _ = tplquad(integrand, a, b, lambda x: a, lambda x: b, lambda x, y: a, lambda x, y: b)
theoretical_mean /= (b - a)**3

# Calculate the theoretical variance
# Variance is the expected value of the squared distance minus the square of the expected distance
def integrand_squared(z, y, x):
    return (x**2 + y**2 + z**2)

theoretical_mean_squared, _ = tplquad(integrand_squared, a, b, lambda x: a, lambda x: b, lambda x, y: a, lambda x, y: b)
theoretical_mean_squared /= (b - a)**3
theoretical_variance = theoretical_mean_squared - theoretical_mean**2

# Simulate 1000 random points in the cube [-1, 1] x [-1, 1] x [-1, 1]
points = uniform.rvs(size=(1000, 3), loc=-1, scale=2)

# Calculate the distance of each point from the origin
distances = np.sqrt(np.sum(points**2, axis=1))

# Calculate the empirical mean distance
empirical_mean_distance = np.mean(distances)

# Calculate the empirical variance of the distances
empirical_variance_distance = np.var(distances)

# Print the results
print(f"Empirical Mean distance from the origin: {empirical_mean_distance:.4f}")
print(f"Empirical Variance of the distances: {empirical_variance_distance:.4f}")
print(f"Theoretical Mean distance from the origin: {theoretical_mean:.4f}")
print(f"Theoretical Variance of the distances: {theoretical_variance:.4f}")
