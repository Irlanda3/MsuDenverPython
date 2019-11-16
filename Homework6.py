#%%
#homework 6
'''if i use numpy array no tengo a hacer loop. en cambio en una lista
si tengo que iterar. numpy array usa menos memonoria y es mas rapido
numpy array usa pointers.
los vectores sirven para los arrays y los vurve plotss.
puedo crear una lista para representar un vector, o tuple 
Vectors have length and direction.
 With numpy, a wide range of mathematical operations can be done directly on
complete arrays, thereby removing the need for loops over array elements. This
is commonly called vectorization

'''
import numpy as np
from math import pi, sqrt, exp
from matplotlib import pyplot as plt
#To create a new array of length n, filled with zeros, we write

# a = np.zeros(10)
# print(a)

def f(x):
    (1 / sqrt(2*pi))**exp(-(0.5)**x**2)
    return
#apply func to a vector x = 
#x = np.linspace(0, 4)
print(f(4))
# %%

import numpy as np

1 /sqrt(2*np.pi)*np.exp**(-1/2)


# %%
import numpy as np
import matplotlib.pyplot as plt
#domain
x=np.linspace(-4,4,100)
#todos los metodos tienen que usar np. esto seria .5*x^2
h=1/np.sqrt(np.pi*2)*np.exp(-0.5*x**2)

plt.plot(x,h)
plt.xlabel("X-axis")
plt.xlabel("Y-axis")
plt.title("h(x)")
plt.xlim([-4,4])
plt.show()

# %%
