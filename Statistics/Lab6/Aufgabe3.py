import numpy as np
from scipy.stats import expon, uniform

# Probabilities for each printer
prob_D1 = 0.4
prob_D2 = 0.6

# Parameters for exponential distribution for D1
scale_D1 = 5  # Mean of the exponential distribution is the inverse of lambda (1/lambda)

# Parameters for uniform distribution for D2
loc_D2 = 4    # Start of the uniform distribution interval
scale_D2 = 2  # Length of the uniform distribution interval

# Number of simulations
N = 10000

# Simulate printing times for D1 and D2
print_times_D1 = expon(scale=scale_D1).rvs(size=N)
print_times_D2 = uniform(loc=loc_D2, scale=scale_D2).rvs(size=N)

# Decide which printer is chosen for each print job
chosen_printer = np.random.choice(['D1', 'D2'], p=[prob_D1, prob_D2], size=N)

# Assign print times based on chosen printer
print_times = np.where(chosen_printer == 'D1', print_times_D1, print_times_D2)

# Calculate probabilities and statistics
probability_more_than_5_seconds = np.mean(print_times > 5)
mean_printing_time = np.mean(print_times)
std_printing_time = np.std(print_times)

# Print the results
print(f"a) Estimated probability of printing taking more than 5 seconds: {probability_more_than_5_seconds:.4f}")
print(f"b) Estimated mean printing time: {mean_printing_time:.2f} seconds")
print(f"   Estimated standard deviation of printing time: {std_printing_time:.2f} seconds")
