import numpy as np

urn = {'red': 20, 'blue': 15, 'green': 5, 'black': 10}

Ns = [200, 1000, 5000]

for N in Ns:
    draws = np.random.choice(list(urn.keys()), size=N, replace=True)

    print(f"\nResults for {N} simulations:")
    for i in range(10):
        color = draws[i]
        relative_frequency = draws[:i + 1].tolist().count(color) / (i + 1)
        print(f"Draw {i + 1}: {color.capitalize()} - Relative Frequency: {relative_frequency:.4f}")

    theoretical_probabilities = {color: count / sum(urn.values()) for color, count in urn.items()}

    simulated_relative_frequencies = {color: draws.tolist().count(color) / N for color in urn.keys()}

    print("\nTheoretical Probabilities:")
    for color, probability in theoretical_probabilities.items():
        print(f"{color.capitalize()}: {probability:.4f}")

    print("\nSimulated Relative Frequencies:")
    for color, frequency in simulated_relative_frequencies.items():
        print(f"{color.capitalize()}: {frequency:.4f}")
