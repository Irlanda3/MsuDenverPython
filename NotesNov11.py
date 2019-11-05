''' scy tools y los animations del chapter 5
en examen 3 no va a venir preguntas de animacion
este dia hicmos animacions de los archivos que estan en jupyter shared_data
tmb vimos color picker como lo vi en w3schools
verctorize cosas'''
#%%
from matplotlib import use, pyplot as plt
import numpy as np

plt.switch_backend('Agg')  # this is a non-interactive backend that prevents the figure from being displayed

def f(x):
    y = []
    for n in x:
        if n >= 0 and n < np.pi/4:
            y.append(np.cos(n))
        else:
            y.append(np.sin(n))
    return y

x = np.linspace(0, np.pi/2, 101)
y = f(x)

fig = plt.figure() #just some space to put axes...basically an empty box 
ax1 = fig.add_subplot(2,2,1)
ax1.plot(x, y, label="Continuous Function")
plt.title("Piecewise")
plt.ylim(0,1)
ax2 = fig.add_subplot(2,2,3)
ax2.plot(x, np.cos(x), label="Cosine", color="g")
plt.title("Cosine")
plt.ylim(0,1)
ax3 = fig.add_subplot(2,2,4)
ax3.plot(x, np.sin(x), label="Sine", color="r")
plt.title("Sine")
plt.ylim(0,1)
fig.savefig("snoopy.png")

# %%
"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter

plt.switch_backend('Agg')

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

anim = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=25, blit=True)
plt.show()


# %%
from matplotlib import pyplot as plt


''' horizontal line:
y = 3, for x [-1,5]
pts, -1.3  5,3
'''
x = [-1,3]; y = [3,3]
plt.plot(x, y, label = "something")
plt.show()

# %%
'''FF -> F*16^1 + F*16^0 = 15*16^1 + 15*16^0 = 255
0123456789ABCDEF
'''

# %%
import numpy as np

x = np.array([1, 2, 3])
a = x
a[2]= 4
print(x)
print(a)
#it seems like we are pointing to the same array
# %%
import numpy as np
import matplotlib as plt


x = np.array([1, 2, 3])
a = x.copy()
a[2]= 4
print(x)
print(a)
#asi ya no tenemos problemas y cada variable es differente ahora
# %%
#ejemplo incomplet
'''el sudo de np.where(condition, a1, a2)
if cond:
    a1
else:
    a2
    '''
    #help(np.where)

import numpy as np

x = np.linspace(0, np.pi/2, 100)
y = np.where(x < np.pi/4, np.cos(x), np.sin(x))


