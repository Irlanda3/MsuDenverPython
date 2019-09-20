#%%
 

'''1.10 RESULTS: 
0.7978845608028654
0.882496902584595
0.704130653528599'''
import math
from sympy import exp, pi
m = 0
s = 2
x = 1
pie = math.pi

y =  ( 1 / (2*pie)**(1/2)  ) * s

y2 = exp((-1/2) * ( (x - m)/s)**2 )
total = y * y2
print(y)
print(y2)
print(total)



