import numpy as np
import matplotlib.pyplot as plt

N = 1000
urne = []
urne.extend([0] * 10)
urne.extend([1] * 20)
urne.extend([2] * 20)


def get_3_random_balls():
    x = 1
    random_balls = np.random.choice(urne, size=3, replace=False)
    for i in range(len(random_balls)):
        x *= random_balls[i]
    return x


simulations = [get_3_random_balls() for _ in range(N)]

erwartungswert = np.mean(simulations)
varianz = np.var(simulations)

print(f"Erwartungswert des Produktes gespeichert in x: {erwartungswert:.2f}")
print(f"Varianz des Produktes gespeichert in x: {varianz:.2f}")

# absoluten Hfg

unique_values, absolute_Hfg = np.unique(simulations, return_counts=True)
plt.bar(unique_values, absolute_Hfg, align='center', edgecolor='black')
plt.xlabel('Werte von x')
plt.ylabel('Absolute Haufigkeit')
plt.title('Absoluten Haufigkeiten von x')
plt.show()

# theoretical probabilities

total_balls = 50
count_x0 = 10
count_x1 = 20
count_x2 = 20

p_x0 = count_x0 / total_balls
p_x1 = count_x1 / total_balls
p_x2 = count_x2 / total_balls

print(f"Theoretische Wahrscheinlichkeit P(x=0): {p_x0}")
print(f"Theoretische Wahrscheinlichkeit P(x=1): {p_x1}")
print(f"Theoretische Wahrscheinlichkeit P(x=2): {p_x2}")

# plotting

theoretical_values = [0, 1, 2]
theoretical_probabilities = [p_x0, p_x1, p_x2]

plt.bar(theoretical_values, theoretical_probabilities, width=0.4, edgecolor='black')
plt.title('Theoretische Wahrscheinlichkeit')
plt.show()
