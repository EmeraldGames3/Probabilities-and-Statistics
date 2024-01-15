from scipy.stats import randint
import numpy

N=10
a=1
b=13   #12 Monate
c=0
G=[]  #Gewinn/Verlust
for i in range(N):
    R = randint.rvs(a, b, size=6)
    S = set(R)
    c = c + (len(S) < 6)
    if len(S) < 6:
        G.append(6)
    else:
        G.append(-6)

print("Wahrscheinlickeit das mindestens 2 Personen von 6 in demselben Monat geboren sind:", c/N)
print("Mittlerer Gewin/Verlust:", numpy.mean(G))
print("Gewinn/Verlust in 1000 Wetten:", sum(G))