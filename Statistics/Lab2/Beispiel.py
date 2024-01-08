import numpy
from matplotlib.pyplot import axis, plot, figure, show, legend

fig = figure()
axis("square")
axis((0, 1, 0, 1))
X = numpy.random.random(25)
Y = numpy.random.random(25)
plot(X, Y, "bo")
fig.suptitle("Beispiel 1 ", fontweight="bold")
show()
fig = figure()
axis("square")
axis((0, 1, 0, 1))
plot(X, numpy.square(X), "g*")  # zufallige Punkte auf dem Bild der Funktion F(x)=xˆ2
plot(X, numpy.power(X, 4), "mo")  # zufallige Punkte auf dem Bild der Funktion F(x)=xˆ4
plot(X[-1], numpy.square(X[-1]), "g*", label="xˆ2")
plot(X[-1], numpy.power(X[-1], 4), "mo", label="xˆ4")
legend(loc='upper left')
fig.suptitle("Beispiel 2 ", fontweight="bold")
show()
