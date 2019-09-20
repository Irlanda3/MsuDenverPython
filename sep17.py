# %%
from cmath import sqrt


def quadform_keyword(a=1, b=1, c=1):
    x_1 = (-b+sqrt(b**2-4*a*c))/(2*a)
    x_2 = (-b-sqrt(b**2-4*a*c))/(2*a)
    return x_1, x_2


print(quadform_keyword(c=1, b=2, a=3))
print(quadform_keyword(3, 2, 1))

# %%
'''variable keyword parameters:
def quadform_varKeyword(**v):

variable position parameters:need to have same order as used in function
    def quadform_varpos(*v): #the star means we do not know how many  am going to receive

read about dictionaries = A dictionary is a collection which is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have keys and values
'''


def myFunc(A ,B = 10, *C, **D):
    print("A", A, "B = ", B, "C = ", C, "D =", D)
    return

myFunc(A=5, B=11, C=(10,20,25), D={'y':66, 'x':99})

def funnyFunc(q, a):
    print("Q: ", q)
    print("A: ", a)

funnyFunc("what is the weather tomorrow?",\
    "Sunny with a chance of sun.") #| add a new line

        

#%%
#Lab 4
import matplotlib.pyplot as plt
from math import pi, exp

def normal_probDesityFunc(x, mu, sigma):
#sigma is standard deviation = 1, mean = 0

    y = 1 / (sigma *sqrt(2*pi) )

    expon = exp(-(.5)*((x - mu)/sigma)**2)

    junto = y*expon
    print(junto)
    # Create the plot
    plt.plot(junto)

    # Show the plot
    plt.show()
    return

normal_probDesityFunc(0, 0, 1) #asi como se dan los parameters asi aqui en ordern tmb




#%%
# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
x = np.array(range(100))
y = x ** 2

# Create the plot
plt.plot(x,y)

# Show the plot
plt.show()


#%%
#Lab 4 part 3
''' use linspace
'''
mu = 0
sigma = 1
a = -3
b = 3.0
n = 10
from numpy import linspace


from math import pi, exp, sqrt

def normal(x, mu, sigma):
#sigma is standard deviation = 1, mean = 0

    y = 1 / (sigma *sqrt(2*pi) )
    expon = exp(-(.5)*((x - mu)/sigma)**2)#si no quieres que te salga j al final importa sqrt no nadamas lo pongas asi


    junto = y*expon
    #print(junto)
    return junto #regresamos esto para saber el valor de esto en

x = linspace(a, b, n)#this will set up x as a list

for y in x:

    z = normal(y, mu, sigma)
    print(z)


#%%
