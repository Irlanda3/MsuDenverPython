# %%
import math


def calcular(t):
    exponente = math.exp(-t)
    seno = math.sin(math.pi*t)
    total = exponente*seno
    print("EXPONENTE: ",exponente)
    print("g(t): ", total)
    return

calcular(0)
calcular(1)

'''EXPONENTE:  1.0
g(t):  0.0
EXPONENTE:  0.36787944117144233
g(t):  4.505223801027239e-17'''

#%%
