# %%
import matplotlib.pyplot as plt
import sys
import numpy as np

# to start reading from 1 en adelante
v = sys.argv[1:]
print(v)
g = 9.81

for v0 in v:
    v0 = eval(v0)
    time = np.arange(1, 2*(v0/g), 0.01)
    y = [((v0 * t) - (0.5 * g * t * t)) for t in time]
    plt.plot(time, y)
    plt.contour(True)

plt.show()

# %%
