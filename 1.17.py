#%%


'''1.17 RESULTS:
(-1+3.872983346207417j) (-1-3.872983346207417j). the problem here is that
var q is holding a negative number
'''
from math import sqrt
import cmath
a = 2
b = 1
c = 2

q = b*b - 4*a*c
print(q)
q_sr = cmath.sqrt(q)
x1 = (-b + q_sr)/2*a
x2 = (-b - q_sr)/2*a
print (x1, x2)