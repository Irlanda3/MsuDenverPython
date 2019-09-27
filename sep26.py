#%%
#LAB 07
import math

def cendiff(f,x,h=1e-05):
    # es f of algo

    r = (f(x + h) - f(x - h))/float(2*h)
    return r
#Part b

dif_1 = lambda x: x + math.exp(x)
print(cendiff(dif_1, 0, .01))# arguments x, f, h

dif_2 = lambda x: 1.0 + math.exp(-2*x**(2))
print(dif_2(0))

print("ERROR: {e:12.5e}".format(e = abs(cendiff(dif_1,0.0,0.01)-dif_2(0.0))))
# el .5 significa 5 decimales y la e es e a la 5 decinamles
# 7+ 5 son 12 espacios en total





#%%
import sympy

def cendiff(f,x,h=1e-05):
    return (f(x+h)-f(x+h)) / (2*h)

x = sympy.symbols('x')
f = x + sympy.exp(x)
fp = sympy.diff(f,x)

f = sympy.lambdify(x,f)
fp = sympy.lambdify(x, fp)


#%%
from math import sin, cos, pi, sqrt

def length(p0, p1):
    """
    inputs:
        p0: (x_1, y_0)
        p1: (x_1, y_1)
    output:
        distance between p0 anf p1
    """
    return sqrt((p1[0] - p0[0])**2 + (p1[1] - p0[1])**2)

def approx(P): #we send a list of points
    L = 0.0
    for K in range(1, len(P)):
        L+= length(P[K-1], P[K])
    return L

n = 20
x = [ 0.5*cos(2.0*pi*i/n) for i in range(n+1)] 
y = [ 0.5*sin(2.0*pi*i/n) for i in range(n+1)] 
print(abs(approx(tuple(zip(x,y))) -pi ))



#%%
