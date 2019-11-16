#%%
import numpy as np 

def f(x):
    #x is an array
    '''for k in range(len(x)):
        x[k]
        '''

    y = np.zeros_like(x)
    for k,v in enumerate(x):#v grabs x
        if v < np.pi/4:
            y[k] = 

# %%
'''aprender np.where
'''
def fvector(x):
    y = np.where(x < np.pi/4, np.cos(x), np.sin(x))
    return y
print(x < np.pi/4)
# %%
''' CHAPTER 6 DE LIBRO  HOY 11/7/2019
'''
#create a dictionary
d = {}

#dictionaries are key value pairs
temps = {'oslo':13, 'london':15.4, 'paris':17.5}

#create a dictionary from string keys
d = dict(sam=56, robert=72, beth=83)
print(d)

#updating values for a particular key
d.update(Sam=66)
print(d)

# accessing value for a particular k
temps['oslo']

for city in temps: #grabbing the keys
    print("the temperature in {:s} is {:g}".format(city, temps[city]))

temps['madrid'] = 26.0
print(temps)


# %%
