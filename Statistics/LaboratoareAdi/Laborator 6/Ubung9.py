import numpy as np
from itertools import permutations, combinations

# a) generate all permutations of the string 'mutig'

string = 'mutig'
all_permutations = list(permutations(string))
print(all_permutations)

# b) generate two random permutations of the string 'mutig'

random_permutations = np.random.choice([''.join(perm) for perm in all_permutations], 2)   # we need each separate letter in 'mutig', thats why we need to split the word into characters
print(random_permutations)

# c) all variations with 4 letters. How many are there?

variations_with_4_letters = list(permutations(string, 4))
print(variations_with_4_letters)
print(f"There are a total of {len(variations_with_4_letters)} variations with 4 letters")

# d) generate all combinations of 2 letters in the string. How many are there?

combinations_of2_letters = list(combinations(string, 2))
print(combinations_of2_letters)
print(f"There are a total of {len(combinations_of2_letters)} combinations of 2 letters")
