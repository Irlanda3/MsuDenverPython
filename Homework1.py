#%%
#Anayeli Ochoa | Homework # 1
'''Chapter 1 Exercises:  1.3, 1.4, 1.6, 1.9, 1.10, 1.12, 1.15, 1.16, 1.17, 1.18
Exercise 1.3: Derive and compute a formula
Can a newborn baby in Norway expect to live for one billion (10^9) seconds? Write
a Python program for doing arithmetics to answer the question.
Filename: seconds2years.
This homework is due on Thursday, September 5, 2019 at the beginning of class.
'''
#Ex 1.3

billion_sec = 10**9
print(billion_sec) # 1,000,000,000

#how many hours is that. sec to hrs
sec_to_min = billion_sec / 60
print(sec_to_min)

min_to_hrs = sec_to_min / 60
print(min_to_hrs, "Hours")

hrs_to_days = min_to_hrs / 24
print(hrs_to_days," Days can a baby live")

days_to_years = hrs_to_days / 365
print("total years", days_to_years)

if days_to_years > 1:
    print("THIS IS NOT CONSIDER A NEW BORN! IT is an adult of", days_to_years," Years!")





'''RESULTS:
1000000000
16666666.666666666
277777.77777777775 Hours
11574.074074074073  Days can a baby live
total years 31.709791983764582
THIS IS NOT CONSIDER A NEW BORN! IT is an adult of 31.709791983764582  Years!

'''

#%%
''' 1.4
Exercise 1.4: Convert from meters to British length units
Make a program where you set a length given in meters and then compute and write
out the corresponding length measured in inches, in feet, in yards, and in miles. Use
that one inch is 2.54 cm, one foot is 12 inches, one yard is 3 feet, and one British
mile is 1760 yards. For verification, a length of 640 meters corresponds to 25196.85
inches, 2099.74 feet, 699.91 yards, or 0.3977 miles.
Filename: length_conversion.'''

#val = raw_input("enter a number in meters: ")
#print(val)


length_in_meters = 640
inches = 39.37*length_in_meters
feet = 3.28*length_in_meters
yards = 1.0936*length_in_meters
miles = 0.0006*length_in_meters

print("640 meters is equal to the following British units")
print(inches," inches")
print(feet, " feet")
print(yards," yards")
print(miles, "miles")

'''RESULTS:
640 meters is equal to the following British units
25196.8  inches
2099.2  feet
699.904  yards
0.38399999999999995 miles'''

#%%
'''1.6
Exercise 1.6: Compute the growth of money in a bank
Let p be a bank’s interest rate in percent per year. An initial amount A has then
grown to A
after n years. Make a program for computing how much money 1000 euros have
grown to after three years with 5 percent interest rate.
Filename: interest_rate.

RESULTS: Interest rate:  1102.5
'''

A=1000
P=5
n=2

formula = A * (1 + (P/100))**n
print("Interest rate: ", formula)

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





#%%
'''1.12
RESULTS:

'''




#%%
'''1.15 RESULTS: variables need to be declared first in order to use them
'''
C = A + B
A = 3
B = 2
print C


#%%
'''1.16 RESULTS:3.141592653589793
-1.2246467991473532e-16
-2.6535897933620727e-06. a variable cannot start with a number
 and many other syntax errors. tan of pi must be a real number

'''
import cmath
import math
a2 = 2
a1 = b
x = 2
y = 4
y2 = x + y # is it 6?
from math import tan
var3 = math.pi
print(var3)
print (math.tan(var3))

pi = 3.14159
print (tan(pi))
c = 4**3**2**3
variable3 = ((c-78564)/c + 32)
discount = 12#%
AMOUNT = 120.#-
amount = 120#$
address = "hpl@simula.no"
variable_and = "duck"
classe = "INF1100, gr 2"
continue_ = x > 0
rev = fox = True
Norwegian = ["a human language"]
true = fox is rev in Norwegian

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

#%%
''' 1.18 ONLY FIND THE ERROR. RESULTS: variable tan needs to have a different
name. also print needs a parenthesis
'''
from math import pi, tan
tan1 = tan(pi/4)
tan2 = tan(pi/3)
print tan1, tan2

#%%
