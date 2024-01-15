import random

anzahl_simulationen = 1000

#1.
#a)
count_rot = 0
for _ in  range(anzahl_simulationen):
    kugeln = random.sample(['r', 'b', 'g'], counts=[6, 4, 6], k = 3)
    if 'r' in kugeln:
        count_rot += 1

thW = 1 - (10/16 * 9/15 * 8/14)
prW = count_rot/anzahl_simulationen
print (f'theoretische Warscheinlichkeit = {thW}, praktische Wahrscheinlichkeit = {prW}')

#b)
count_dieselbe_farbe = 0
for _ in range(anzahl_simulationen):
    kugeln = random.sample(['r', 'b', 'g'], counts=[6, 4, 6], k = 3)
    if len(set(kugeln)) == 1:
        count_dieselbe_farbe += 1

thW = 6/16 * 5/15 * 4/14 + 4/16 * 3/15 * 2/14 + 6/16 * 5/15 * 4/14
prW = count_dieselbe_farbe/anzahl_simulationen
print (f'theoretische Warscheinlichkeit = {thW}, praktische Wahrscheinlichkeit = {prW}')

#c)
count_rot_und_dieselbe_farbe = 0
for _ in range(anzahl_simulationen):
    kugeln = random.sample(['r', 'b', 'g'], counts = [6, 4, 6], k = 3)
    if 'r' in kugeln and len(set(kugeln)) == 1:
        count_rot_und_dieselbe_farbe += 1

thW = 6/16 * 5/15 * 4/14
prW = count_rot_und_dieselbe_farbe/anzahl_simulationen
print (f'theoretische Warscheinlichkeit = {thW}, praktische Wahrscheinlichkeit = {prW}')

#d)
count1 = 0
for _ in range(anzahl_simulationen):
    kugeln = random.sample(['r', 'b', 'g'], counts = [6, 4, 6], k = 3)
    if len(set(kugeln)) == 1 and 'r' in kugeln:
        count1 += 1

wahrscheinlichkeit1 = count1/anzahl_simulationen

count_rot = 0
for _ in  range(anzahl_simulationen):
    kugeln = random.sample(['r', 'b', 'g'], counts=[6, 4, 6], k = 3)
    if 'r' in kugeln:
        count_rot += 1

wahrscheinlichkeit2 = count_rot/anzahl_simulationen

thW = (6/16 * 5/15 * 4/14) / (1 - (10/16 * 9/15 * 8/14))
prW = wahrscheinlichkeit1/wahrscheinlichkeit2
print (f'theoretische Warscheinlichkeit = {thW}, praktische Wahrscheinlichkeit = {prW}')