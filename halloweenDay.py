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
plt.plot(x, y2, label="Cosine Function")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Our first plot(s)")
plt.show()# este siempre debe ir al ultimo para q grafique todo

# %%
from matplotlib import pyplot as plt
import numpy as np  # para poder usar linspace
from math import exp

fnc = x**2*exp(-x**2)#from 0 to 4
plt.plot(x, label="Exponential function")
plt.legend()
plt.show()

# %%
from matplotlib import pyplot as plt
import numpy as np  # para poder usar linspace
from math import exp

x = np.linspace(0,4,65)# el 65 representa cuanto snumeros quieres
y = x**2*np.exp(-x**2)
plt.plot(x,y, label = "x^2 e^(-x^2)", marker = "o", linestyle = "None")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Nice Function")
plt.xlim(0,3)#tmb podemos decir xmax=3, xmin=0
plt.show()
'''podemos usar help(plt)
label es un keyword argument, x and y son positional
'''

# %%
from matplotlib import pyplot as plt
import numpy as np  # para poder usar linspace
from math import exp

x = np.linspace(0,4,65)# el 65 representa cuanto snumeros quieres
y = x**2*np.exp(-x**2)
plt.plot(x,y, "r-.", label = "x^2 e^(-x^2)",)
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Nice Function")
plt.xlim(0,3)#tmb podemos decir xmax=3, xmin=0
plt.show()
'''podemos usar help(plt)
label es un keyword argument, x and y son positional
'''


# %%
