#%%
'''estamos aprendiendi global variables
'''
a=20
b=-2.5 #this are global avariables
def f1(x):
    a=21 #this is a local variable
    return a*x +b

print(a)

def f2(x):
    global a #global variable
    a = 21
    return a*x+ b #regresar para poder usarlo donde queramos

f1(3); print(a)
f2(3); print(b)# output debe ser 20,20,21


#%%
print(sum)#sum is a keyword or built in function
sum= 500 #global variable
print(sum) #imprime 500

def muyfunc(n):
    sum = n+ 1 # aqui ya es local variable
    print(sum)
    return sum
sum = muyfunc(2) +1 #imprime la locla variable
print(sum)



#%%
print(sum)#sum is a keyword or built in function
sum= 500 #global variable
print(sum) #imprime 500

def muyfunc(n):
    global sum  #es para usar la sum global de arriva osea aqui la cambiamos la podemos manipular
    sum = n+ 1 # aqui ya es local variable
    print(sum)
    return sum

new_sum = muyfunc(2) + 1 #imprime la locla variable
print(sum)
print(new_sum)



#%%
def a(x):
    q = 2
    x = 3*x
    return q + x

def b(x):
 global q
 q += x
 return q + x

q = 0
x = 3
print(a(x), b(x), a(x), b(x))



#%%
#este hace lo mismo que la cell anterior pero la sintax es diferente
def a(x):
    q = 2
    x = 3*x
    return q + x

def b(x,q):
 #global q
    q = x + q
    return q + x, q

q = 0
x = 3
result_1 = a(x)
result_2, q = b(x,q)
result_3 = a(x)
result_4, q = b(x,q)
print(result_1, result_2, result_3, result_4)
#print(a(x), b(x), a(x), b(x))

#%%
#exercise rcos(angle), rsin(angle)
from math import cos, sin, pi


def coordinates(r=1.0, a=0.0):
    return r * cos(a), r*sin(a)

c = coordinates(a=pi/4.0)
print(c)
    
    
    





#%%
def coordinates(r=1.0, a=0.0):
    """computes the coordinate pair
    of a circle of radius r and angle a
    input:
    r: radius as float
    a: angle in radius as float
    output:
    tuple(x,y) as float
    """
    return r * cos(a), r*sin(a)

c = coordinates(a=pi/4.0)
print(c)

#r es un keyword y automaticamente pondria 1 aun que yo no lo ponga



#%%
'''assert function
I have a picture in my cellphone
'''


