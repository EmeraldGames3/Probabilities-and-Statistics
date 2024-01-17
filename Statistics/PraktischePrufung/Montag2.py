"""
Die Zufallsgröße Y ist gegeben durch

P (X = 1) = 0.4, P (Y = 2) = 0.6.

(a) Experiment: Man generiert 3 zufällige Werte für Y. Sei Z die Zufallsgröße die anzeigt wie oft die 2 unter diesen
3 Werten auftaucht (z.B. [2,1, 1] → Z = 1; [1, 1, 1] → Z = 0 usw.)

Man generiere 2000 zufällige Werte für die Zufallsgröße Z. Man gebe jeden möglichen Wert von Z und die entsprechende
relative hfg an mit print -> hat die relative Hfg.= ...")).

(B) man gebe die theoretische wharscheinlichkeitsverteilung von Z an  dh alle theoretische werte die Z annehmen kann
und die entsprechenden Wahrscheinlichkeiten zb mit print() annehmen kann und die entsprechenden Wahrscheinlichkeiten,
zB. mit print (f" P (Z=. ..)=...").

(c) Man zeichne das Histogramm der relativen Häufigkeiten von den 2000 simulierten Werten für Z.

(d) Man schätze die Wahrscheinlichkeit P({Z = 0} oder {Z = 3}) und gebe den theoretischen Wert an für P({Z = 0} oder
{Z=3}).
"""
import random
import matplotlib.pyplot as plt

# Funktion zur Generierung von 3 zufälligen Werten für Y und Berechnung von Z
def generate_Z():
    Y = [random.randint(1, 6) for _ in range(3)]
    return Y.count(2)

# Simuliere 2000 Zufallsereignisse für Z
simulated_values = [generate_Z() for _ in range(2000)]

# Berechne relative Häufigkeiten
relative_frequencies = {i: simulated_values.count(i) / 2000 for i in set(simulated_values)}

# Gebe jeden möglichen Wert von Z und die entsprechende relative Häufigkeit aus
print("Z   Relative Häufigkeit")
for value, frequency in sorted(relative_frequencies.items()):
    print(f"{value}   {frequency:.4f}")

# Theoretische Wahrscheinlichkeitsverteilung von Z
theoretical_distribution = {0: (5/6) ** 3, 1: 3 * (1/6) * (5/6) ** 2, 2: 3 * (1/6) ** 2 * (5/6), 3: (1/6) ** 3}

# Gebe die theoretischen Werte und ihre Wahrscheinlichkeiten aus
print("\nTheoretische Wahrscheinlichkeitsverteilung:")
for value, probability in sorted(theoretical_distribution.items()):
    print(f"{value}   {probability:.4f}")

# Histogramm der relativen Häufigkeiten
plt.bar(relative_frequencies.keys(), relative_frequencies.values(), width=0.5, align='center', alpha=0.7)
plt.title('Histogramm der relativen Häufigkeiten von Z')
plt.xlabel('Z')
plt.ylabel('Relative Häufigkeit')
plt.show()