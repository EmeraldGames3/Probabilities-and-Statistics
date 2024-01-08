import random
import numpy

# Initialize counters
c1, c2, a1, a2 = 0, 0, 0, 0
N = 10000  # Number of simulations
A = list(range(1, 21))  # List from 1 to 20

# Simulate N times
for _ in range(N):
    i = numpy.random.randint(len(A))
    v = A[i]
    c1 += (v % 2)  # Count odd numbers
    c2 += ((v % 2) == 0)  # Count even numbers
    a1 += (v % 2) * ((v % 3) == 0)  # Count odd numbers divisible by 3
    a2 += ((v % 2) == 0) * (6 <= v and v <= 10)  # Count even numbers between 6 and 10

# Calculate estimated probabilities
p1 = a1 / c1 if c1 != 0 else 0
p2 = a2 / c2 if c2 != 0 else 0
p3 = c1 / N

# Print estimated probabilities
print("Aus den Simulationen:")
print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p3 = {p3}")

# Theoretical calculations
# p1: Probability that a number is divisible by 3 given that it is odd
odd_div_by_3 = len([num for num in range(1, 21) if num % 2 != 0 and num % 3 == 0])
total_odd = len([num for num in range(1, 21) if num % 2 != 0])
theoretical_p1 = odd_div_by_3 / total_odd

# p2: Probability that a number is between 6 and 10 given that it is even
even_6_to_10 = len([num for num in range(6, 11) if num % 2 == 0])
total_even = len([num for num in range(1, 21) if num % 2 == 0])
theoretical_p2 = even_6_to_10 / total_even

# p3: Probability of an odd number
theoretical_p3 = total_odd / 20

# Print theoretical probabilities
print("\nTheoretische Werte:")
print(f"Theoretisches p1 = {theoretical_p1}")
print(f"Theoretisches p2 = {theoretical_p2}")
print(f"Theoretisches p3 = {theoretical_p3}")
