import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom


n_recomputers = 7
p_virus_attack = 0.4

N = 10000
simulated_values = binom.rvs(n_recomputers, p_virus_attack, size=N)

simulated_prob_a = np.mean(simulated_values <= 3)
theoretical_prob_a = binom.cdf(3, n_recomputers, p_virus_attack)

simulated_prob_b = np.mean(simulated_values >= 4)
theoretical_prob_b = 1 - binom.cdf(3, n_recomputers, p_virus_attack)

simulated_prob_c = np.mean(simulated_values == 4)
theoretical_prob_c = binom.pmf(4, n_recomputers, p_virus_attack)


print(f"a) Simulated Probability (at most 3 computers): {simulated_prob_a:.4f}, Theoretical Probability: {theoretical_prob_a:.4f}")
print(f"b) Simulated Probability (at least 4 computers): {simulated_prob_b:.4f}, Theoretical Probability: {theoretical_prob_b:.4f}")
print(f"c) Simulated Probability (exactly 4 computers): {simulated_prob_c:.4f}, Theoretical Probability: {theoretical_prob_c:.4f}")

plt.hist(simulated_values, bins=np.arange(-0.5, n_recomputers+1.5, 1), density=True, alpha=0.7, label='Simulated Histogram')

x = np.arange(0, n_recomputers+1)
theoretical_probs = binom.pmf(x, n_recomputers, p_virus_attack)
plt.stem(x, theoretical_probs, linefmt='r-', markerfmt='ro', label='Theoretical Probabilities')

plt.xlabel('Number of Computers Attacked')
plt.ylabel('Probability')
plt.legend()

plt.show()