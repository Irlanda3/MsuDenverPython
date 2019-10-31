# %%
# vimos matplotlib y arrays
'''scy tools es como matplot lib y scytools ya no se usa
on the jupyterhub - not from command line - can from notebook
y se dice: from matplotlib import pyplot as plt
notebook specific:
%matplotlib inline
syntax for basic plot
plt.plot(<x-values>,<y-values>,label = <string>)'''

from matplotlib import pyplot as plt
import numpy as np  # para poder usar linspace

x = np.linspace(-2*np.pi, 2*np.pi, 47)
y1 = np.sin(x)  # le hacemos el sin de ese array
y2 = np.cos(x)

plt.plot(x, y1, label="Sine Function")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Our first plot(s)")
plt.show()

# %%
