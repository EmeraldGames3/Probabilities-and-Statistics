import numpy as np
import matplotlib.pyplot as plt

N = 1000
urne = []
urne.extend(['red'] * 20)
urne.extend(['blue'] * 15)
urne.extend(['green'] * 5)
urne.extend(['black'] * 10)


def get_random_balls():
    random_balls = np.random.choice(urne, size=1, replace=True)
    return random_balls


simulations = [get_random_balls() for _ in range(N)]

unique_counts, relative_freq = np.unique(simulations, return_counts=True)
relative_freq = relative_freq / N

color_order = ['red', 'blue', 'green', 'black']

# theoretical probabilities
total_balls = 50
red_balls = 20
blue_balls = 15
green_balls = 5
black_balls = 10

p_red_balls = red_balls / total_balls
p_blue_balls = blue_balls / total_balls
p_green_balls = green_balls / total_balls
p_black_balls = black_balls / total_balls

theoretical_probabilities = [p_red_balls, p_blue_balls, p_green_balls, p_black_balls]

plt.bar(color_order, relative_freq[np.argsort(color_order)], align='center', label='relative Hfg')   # need the argsort to keep the correct order of the colors in the plot
plt.bar(color_order, theoretical_probabilities, align='center', width=0.4, edgecolor='black', linewidth=2, label='theoretische Hfg')
plt.title(f"Relative Haufigkeit aufgeteilt auf Farben in {N} Experimente")
plt.xlabel('Farben')
plt.ylabel('Relative Haufigkeit/Theoretische Haufigkeit')
plt.legend()
plt.show()

# results from the first 10 picks -> set N = 10, if there is an error, that is because in these 10 picks,
# there is at least one color that is missing.
# So the solution would be to set the default value of any color to be 0 if it can't be picked in the
# number of simulations that has been set
