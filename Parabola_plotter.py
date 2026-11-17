import math
import matplotlib.pyplot as plt

x = []
y = []

for x in range (-6,8):
    calc = x**2
    x.append()
    y = y + calc
    y.append()


plt.plot(x)
plt.xlabel("Horizontal Axis")
plt.plot(y)
plt.ylabel("Vertical Axis")

plt.savefig("ParabolaGraph.png")
