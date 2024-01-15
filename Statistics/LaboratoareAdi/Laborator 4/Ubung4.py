import scipy
import numpy
from matplotlib.pyplot import bar, show, hist, grid, legend, xticks

# a)
N = 1000
n = 7
p = 0.4
vector = [0, 1, 2, 3, 4, 5, 6, 7]

count_max_3_viruses = 0
for i in range(n+1):
    if i < 4:
        count_max_3_viruses += 1

count_min_4_viruses = 0
for i in range(n+1):
    if i > 4:
        count_min_4_viruses += 1

count_4_viruses = 0
for i in range(n+1):
    if i == 4:
        count_4_viruses += 1




