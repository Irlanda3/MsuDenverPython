#%%
'''1.9
Type in programs and debug them
RESULTS: I get an error that says invalid token, and I added import math
and change the syntax
1.0000000000000002
'''

#a) Does sin^2(x) + cos^2(x) = 1?

import math

z =math.pi/4
a = math.sin(z)**2 +math.cos(z)**2
print(a, round(a, 1))

#partb RESULTS: 4.0

v0 = 3 #m/s
t = 1  #s
a = 2  #m/s**2
s = v0*t + 0.5*a*t**2
print (s)

#partc RESULTS: First equation: %g = %g 73.96 73.96
#Second equation: %h = %h 4.0 4.0


a = 3.3
b = 5.3
a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print ("First equation: %g = %g"  ,  eq1_sum, eq1_pow)
print ("Second equation: %h = %h",  eq2_pow, eq2_pow)
