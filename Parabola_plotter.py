"""
Parabola Plotter
Amelia Addis
This program creates a physical graph of a parabola that changes as the range does.
11/16/2026
"""

import math
import matplotlib.pyplot as plt

x = []
y = []

for number in range (-6,8):
    calc = number**2
    x.append(number)
    y.append(calc)


plt.plot(x, y)
plt.xlabel("Horizontal Axis")
plt.ylabel("Vertical Axis")
plt.title("Parabola Graph")

plt.savefig("ParabolaGraph.png")
plt.show()
