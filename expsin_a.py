# %%
'''Print out h.0/ and h.1/ for the case a D 10.
OUTPUT:
EXPONENTE:  1.0
h(t):  0.0
EXPONENTE:  4.5399929762484854e-05
h(t):  5.559887866514173e-21
'''
import math


def calcular(t, a):
    exponente = math.exp(-(a*t))
    seno = math.sin(math.pi*t)
    total = exponente*seno
    print("EXPONENTE: ", exponente)
    print("h(t): ", total)
    return


calcular(0, 10)
calcular(1, 10)

# %%
