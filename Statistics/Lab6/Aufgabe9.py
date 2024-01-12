import itertools
import random

# String to be used
s = "mutig"

# a) Generate all permutations of the string "mutig"
permutations = list(itertools.permutations(s))
print(f"a) Total permutations of 'mutig': {len(permutations)}")
print(permutations)

# b) Generate two random permutations of the string "mutig"
random_permutations = random.sample(permutations, 2)
print(f"b) Two random permutations: {''.join(random_permutations[0])}, {''.join(random_permutations[1])}")

# c) Generate all variations with four letters from "mutig"
variations = list(itertools.permutations(s, 4))
print(f"c) Total variations with four letters from 'mutig': {len(variations)}")
print(variations)

# d) Generate all combinations with two letters from "mutig"
combinations = list(itertools.combinations(s, 2))
print(f"d) Total combinations with two letters from 'mutig': {len(combinations)}")
print(combinations)
