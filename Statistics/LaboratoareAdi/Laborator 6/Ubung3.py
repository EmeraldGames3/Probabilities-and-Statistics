from scipy.stats import expon, uniform
import numpy as np

P1 = 0.4
P2 = 0.6

lambda_1 = 1/5
T1 = expon(loc=0, scale=1/lambda_1)

min_T2 = 4
max_T2 = 6
T2 = uniform(loc=min_T2, scale=max_T2 - min_T2)

simulations = 10000

samples_T1 = T1.rvs(size=simulations)
samples_T2 = T2.rvs(size=simulations)

prob_more_than_5 = P1 * np.mean(samples_T1 > 5) + P2 * np.mean(samples_T2 > 5)

erwartungswert = P1 * np.mean(samples_T1) + P2 * np.mean(samples_T2)

standardabweichung = np.sqrt(P1 * np.std(samples_T1)**2 + P2 * np.std(samples_T2)**2)

print(f"Probability that the printer will take more than 5 seconds: {prob_more_than_5:.4f}")
print(f"Weighted Expected Value (gewichteter Erwartungswert): {erwartungswert:.4f}")
print(f"Weighted Standard Deviation (gewichtete Standardabweichung): {standardabweichung:.4f}")
