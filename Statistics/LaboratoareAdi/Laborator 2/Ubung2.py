import numpy as np

#beispiel code

from matplotlib.pyplot import axis, plot, figure, show, legend, Circle, text


# fig = figure()
# axis("square")
# axis((0, 1, 0, 1))
# X = np.random.random(25)
# Y = np.random.random(25)
# plot(X, Y, "bo")
# fig.suptitle("Beispiel 1 ", fontweight = "bold")
# show()
#
# fig = figure()
# axis("square")
# axis((0, 1, 0, 1))
# plot(X, np.square(X), "g*")
# plot(X, np.power(X, 4), "mo")
# plot(X[-1], np.square(X[-1]), "g*", label = "x^2")
# plot(X[-1], np.power(X[-1], 4), "mo", label = "x^4")
# legend(loc = "upper left")
# fig.suptitle("Beispiel 2 ", fontweight = "bold")
# show()


#Ubung2
# a) man simuliere n zufallige Punkte im Quadrat, stelle sie grapisch dar und man zahle wie viele im Kreisinneren sind (k)

def ex2(n):
    fig = figure()
    axis("square")
    axis((0, 1, 0, 1))
    x = np.random.random(n)
    y = np.random.random(n)

    inside_circle = 0
    outside_circle = 0

    for i in range(len(x)):
        distance = np.linalg.norm([x[i] - 0.5, y[i] - 0.5])  # Euclidean distance
        if distance <= 0.5:
            plot(x[i], y[i], "bo")
            inside_circle += 1
        else:
            plot(x[i], y[i], "ro")
            outside_circle += 1

    circle = Circle((0.5, 0.5), 0.5, fill=False, color='r')
    ax = fig.gca()
    ax.add_patch(circle)

    fig.suptitle("Ubung 2 ", fontweight="bold")
    text(0.5, -0.1, f"\n\nPoints inside the circle: {inside_circle}\n",
             horizontalalignment='center', verticalalignment='center')
    show()

ex2(100)