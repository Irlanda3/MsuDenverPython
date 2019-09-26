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
