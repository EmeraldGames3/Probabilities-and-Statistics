import random


def birthday_simulation(num_simulations):
    total_winnings = 0
    successful_bets = 0

    for _ in range(num_simulations):
        birthdays = [random.randint(1, 12) for _ in range(6)]
        if len(birthdays) != len(set(birthdays)):
            successful_bets += 1
            total_winnings += 6
        else:
            total_winnings -= 6

    probability = successful_bets / num_simulations
    average_gain_loss = total_winnings / num_simulations

    return probability, average_gain_loss


def theoretical_probability():
    no_shared_birthday_prob = 1.0
    for i in range(6):
        no_shared_birthday_prob *= (12 - i) / 12

    probability = 1 - no_shared_birthday_prob
    average_gain_loss = -6 * no_shared_birthday_prob + 6 * probability

    return probability, average_gain_loss


num_simulations = 100000
simulated_probability, simulated_avg_gain_loss = birthday_simulation(num_simulations)
theoretical_prob, theoretical_avg_gain_loss = theoretical_probability()

print(f"Theoretical Probability of Winning: {theoretical_prob}")
print(f"Simulated Probability of Winning: {simulated_probability}")
print(f"Theoretical Average Gain/Loss per Bet: {theoretical_avg_gain_loss} euros")
print(f"Simulated Average Gain/Loss per Bet: {simulated_avg_gain_loss} euros")
