import numpy as np

# man schatze durch wiederholte Simulationen die Wahrscheinlichkeit von dem Ereignis A:
# in einer Gruppe von 23 Personen, mindestens zwei Personen haben den gleichen Geburtstag. Man nimmt an 1 Jahr = 365 Tage

def birthday_simulation(num_simulations, group_size):
    count_shared_birthdays = 0

    for _ in range(num_simulations):
        birthdays = np.random.randint(low=1, high=366, size=group_size)

        if len(birthdays) != len(set(birthdays)):
            count_shared_birthdays += 1

    probability = count_shared_birthdays / num_simulations

    return probability

num_simulations = 1000
group_size = 23
result = birthday_simulation(num_simulations, group_size)

print(f"The simulated probability of at least two people having the same birthday in a group of {group_size} is approximately {result:.2f}")

def theoretical_prob(group_size):
    probability_no_shared_bday = 1.0
    for i in range(group_size):
        probability_no_shared_bday *= (365 - i) / 365

    return 1 - probability_no_shared_bday

th_prob = theoretical_prob(group_size)
print(f"The theoretical probability of at least two people having the same birthday in a group of {group_size} is {th_prob:.2f}")
