import numpy as np
import math

group_size = 5
simulations = 10000
count_shared_birthmonths = 0
for _ in range(simulations):
    birthmonths = np.random.randint(low=1, high=13, size=group_size)

    if len(birthmonths) - len(set(birthmonths)) == 1:
        count_shared_birthmonths += 1

probability = count_shared_birthmonths / simulations
print(f"The probability that at exactly 2 people share the same birthmonth in a group of {group_size} people, and the other people have different birthmonths, is {probability}")

# theoretical way to get the probability

months = 12
same_birthday_individuals = math.comb(5, 2)   # combinations of 2 out of 5 people to be chosen to have the same birthday
other_people_birthmonth = 11 * 10 * 9    # the 3rd person can have 11 out of the 12 birthmonths, since it needs to be different from the first two, and the same applies to the other two individuals that can have 10 and 9 birthmonths
total_ways_to_arrange = months * same_birthday_individuals * other_people_birthmonth    # the individuals having the same birthmonth can be ordered in any way, at the beginning, in the middle or at the end
total_outcomes = 12 ** group_size    # 12 possible birthmonths, and there are 5 people in the group

theoretical_probability = total_ways_to_arrange / total_outcomes

print(f"The theoretical probability that at exactly 2 people share the same birthmonth in a group of {group_size} people, and the other people have different birthmonths, is {theoretical_probability}")
