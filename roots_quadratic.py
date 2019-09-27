#%%
import math

def cuadratic(a,b,c):
      

    part_1 = -b - math.sqrt(b - 4*a*c)
    part_2 = -b + math.sqrt(b - 4*a*c)
    negative_x = part_1 / 2*a
    positive_x = part_2 / 2*a
    return positive_x,negative_x#si no regreso nada no muestra nada

cuadratic(5,6,1)


#%%
#import cmath to get complex numbers / imaginary
#from numpy.lib.scimath import sqrt
'''z = a + bi where a is the real part and b is the imaginary part.'''
#def cuadratica(a=1,b=6,c=2): 
#def cuadratica(a=1,b=-1,c=-6):  #x=3 , x=−2 
#def cuadratica(a=1,b=-2,c=5):#numero complex
#from cmath import sqrt#The cmath functions always return complex numbers
from numpy.lib.scimath import sqrt as csqrt
def roots(a,b,c):

    r1 = (-b + csqrt(b**2 - 4*a*c))/(2*a)
    r2 = (-b - csqrt(b**2 - 4*a*c))/(2*a)

    print(r1.imag,"imaginario")
    print(r2.real,"real")
    return r1, r2#si no regreso nada no muestra nada
#roots(1,-2,5)#imaginario
roots(5,6,1)

#cuadratic(1,-1,-6)
#cuadratic(1,-2,5)



#%%
from numpy.lib.scimath import sqrt as csqrt
a = 5; b = 6; c = 1 # polynomial coefficients

r1 = (-b + csqrt(b**2 - 4*a*c))/(2*a)
r2 = (-b - csqrt(b**2 - 4*a*c))/(2*a)
print(r1)
print(r2)


#%%
