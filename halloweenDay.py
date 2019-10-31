# %%
# vimos matplotlib y arrays
'''scy tools es como matplot lib y scytools ya no se usa
on the jupyterhub - not from command line - can from notebook
y se dice: from matplotlib import pyplot as plt
notebook specific:
%matplotlib inline
syntax for basic plot
plt.plot(<x-values>,<y-values>,label = <string>)'''

from math import exp
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
plt.show()  # este siempre debe ir al ultimo para q grafique todo

# %%

fnc = x**2*exp(-x**2)  # from 0 to 4
plt.plot(x, label="Exponential function")
plt.legend()
plt.show()

# %%

x = np.linspace(0, 4, 65)  # el 65 representa cuanto snumeros quieres
y = x**2*np.exp(-x**2)
plt.plot(x, y, label="x^2 e^(-x^2)", marker="o", linestyle="None")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Nice Function")
plt.xlim(0, 3)  # tmb podemos decir xmax=3, xmin=0
plt.show()
'''podemos usar help(plt)
label es un keyword argument, x and y son positional
'''

# %%

x = np.linspace(0, 4, 65)  # el 65 representa cuanto snumeros quieres
y = x**2*np.exp(-x**2)
plt.plot(x, y, "r-.", label="x^2 e^(-x^2)")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Nice Function")
plt.xlim(0, 3)  # tmb podemos decir xmax=3, xmin=0
plt.show()
'''podemos usar help(plt)
label es un keyword argument, x and y son positional
'''


# %%

x = np.linspace(0, 4, 65)  # el 65 representa cuanto snumeros quieres
y = x**2*np.exp(-x**2)
plt.plot(x, y, "g", label="x^2 e^(-x^2)")
plt.plot(x, y, "r-.", label="x^2 e^(-x^2)")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Nice Function")
plt.xlim(0, 3)  # tmb podemos decir xmax=3, xmin=0
plt.show()
'''podemos usar help(plt)
label es un keyword argument, x and y son positional
'''

# %%


def f(x):# x comes in as an array
    y= []
    for n in x:
        if n >= 0 and n < np.pi/4:
            y.append(np.cos(n))
        else:
            y.append(np.sin(n))

    return y


x = np.linspace(0, np.pi/2, 101)#what it means 101 pts? osea q de 101 pts todos iguales 
y = f(x)

plt.plot(x, y, label="Continuous fnc")
plt.plot(x, np.cos(x), label = "Cosine")
plt.plot(x, np.sin(x), label = "Cosine")
plt.show()

# %%
def f(x):# x comes in as an array
    y= []
    for n in x:
        if n >= 0 and n < np.pi/4:
            y.append(np.cos(n))
        else:
            y.append(np.sin(n))

    return y


x = np.linspace(0, np.pi/2, 101)#what it means 101 pts? osea q de 101 pts todos iguales 
y = f(x)

plt.subplot(1, 3, 1)#row 1 osea que tendremos una linea con 3 imagenes, y el sig 1 es la primera grap
plt.plot(x, y, label="Continuous fnc")
plt.ylim(0,1)

plt.subplot(1, 3, 2)
plt.plot(x, np.cos(x), label = "Cosine")
plt.ylim(0,1)

plt.subplot(1, 3, 3)
plt.plot(x, np.sin(x), label = "Sine", color ="r")
plt.ylim(0,1)

plt.show()

# %%
def f(x):# x comes in as an array
    y= []
    for n in x:
        if n >= 0 and n < np.pi/4:
            y.append(np.cos(n))
        else:
            y.append(np.sin(n))

    return y


x = np.linspace(0, np.pi/2, 101)#what it means 101 pts? osea q de 101 pts todos iguales 
y = f(x)

plt.subplot(1, 3, 1)#row 1 osea que tendremos una linea con 3 imagenes, y el sig 1 es la primera grap
plt.plot(x, y, label="Continuous fnc")
plt.ylim(0,1)

plt.subplot(1, 3, 2)
plt.plot(x, np.cos(x), label = "Cosine")
plt.ylim(0,1)

plt.subplot(1, 3, 3)
plt.plot(x, np.sin(x), label = "Sine", color ="r")
plt.ylim(0,1)

plt.show()

# %%
def f(x):# x comes in as an array
    y= []
    for n in x:
        if n >= 0 and n < np.pi/4:
            y.append(np.cos(n))
        else:
            y.append(np.sin(n))

    return y


x = np.linspace(0, np.pi/2, 101)#what it means 101 pts? osea q de 101 pts todos iguales 
y = f(x)

plt.subplot(1, 3, 1)#row 1 osea que tendremos una linea con 3 imagenes, y el sig 1 es la primera grap
plt.plot(x, y, label="Continuous fnc")
plt.ylim(0,1)

plt.subplot(1, 3, 2)
plt.plot(x, np.cos(x), label = "Cosine")
plt.ylim(0,1)

plt.subplot(1, 3, 3)
plt.plot(x, np.sin(x), label = "Sine", color ="r")
plt.ylim(0,1)

plt.savefig("snoopy.png")# este lo puedes abrir de sde la temrinal

# %%
