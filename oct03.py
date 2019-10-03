#%%
'''eval and exec
r = eval('4+3") y nos da 7 lo evalua
aun que sea string'''

from math import*
x = eval('cos(pi/14)')
y = eval('sin(pi/14)')
print(x,y)

#%%
import sys
from math import *

def midpoint(f, a, b, n=100):
    h = (b-a)/n
    I = 0.0
    for i in range(n):
        
        I += f(a+(i+0.5)*h) * h
        return I
formula = sys.argv[1]
a = float(sys.argv[2])
b = float(sys.argv[3])
n = int(sys.argv[4])

code = "def f(x): return {:s}".format(formula)
exec(code)
print(midpoint(f, a, b, n))

# to run in terminal x**3-2*x+7 0.0 3.0 76
#%%
'''reading files
