#%%
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

'''OUTPUT: A GRAPH'''

# %%
