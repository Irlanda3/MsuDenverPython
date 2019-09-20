#%%
''' Newton's method
'''
from sympy import symbols, diff

x = symbols('x')
f = x**2-3 #fn
dfdx = diff(f, x)

x_old = 1.0
x_new = x_old - ( f.subs(x, x_old) / dfdx.subs(x, x_old) )

#we do not know so use a while loop. == != <= >= 
#logic: and = both need to be true, if one is false returns false. OR= 1 needs to be true. zero or false puede regresar

k = 0
while abs(x_old - x_new) > 0.5e-8:
    x_old = x_new
    x_new = x_old - ( f.subs(x, x_old) / dfdx.subs(x, x_old) )
k+=1
print(x_new)
print(k)

#%%
''' Newton's method now using a for loop
'''
from sympy import symbols, diff

x = symbols('x')
f = x**2-3 #fn
dfdx = diff(f, x)

x_old = 1.0
x_new = x_old - ( f.subs(x, x_old) / dfdx.subs(x, x_old) )

#we do not know so use a while loop. == != <= >= 
#logic: and = both need to be true, if one is false returns false. OR= 1 needs to be true. zero or false puede regresar

k = 0
for q in range(3):#if we change the range we see different decimal numbers
    x_old = x_new
    x_new = x_old - ( f.subs(x, x_old) / dfdx.subs(x, x_old) )
k+=1
print(x_new)
print(k)


#%%
''' TUPLE: collection of objects(immutable)
x = (1,2,3,7,11,15)

LIST: collection of objects(mutable)
x = [1,2,3,7,11,15]
x.append(16)
print(x)
x = [1,2,3,7,11,15,16]
we can also have a list of lists: x = [[1,2,3], [1,2.3]]'''
#elem0, 1,2,3,4 ,5
x =  [1,2,3,7,11,15]
x[3]

print(x[1])
#nested list use x[1][2]



#%%
#lab 3

list_grades = [[ 7.0, 3.0, 7.0, 7.0, 9.0, 0.0, 0.0, 0.0],
[10.0,10.0, 8.0,10.0,10.0,10.0, 1.0,10.0],
[10.0, 0.0, 5.0,10.0, 9.0,10.0, 8.0, 8.0],
[10.0,10.0, 5.0, 2.0,10.0,10.0,10.0, 8.0],
[10.0,10.0, 8.0,10.0, 9.0, 9.0,10.0, 9.0],
[ 9.0, 7.0, 8.0, 7.0, 0.0, 6.0, 6.0, 6.0],
[ 5.0, 0.0, 5.0, 3.0, 2.0,10.0, 6.0, 0.0],
[ 9.0, 8.0, 8.0, 5.0, 7.0, 8.0, 5.0,10.0],
[10.0,10.0, 3.0,10.0, 9.0,10.0,10.0, 8.0],
[ 8.0, 5.0, 7.0, 5.0, 8.0, 8.0, 4.0, 8.0],
[ 8.0, 0.0, 9.0, 0.0, 8.0,10.0, 9.0,10.0],
[ 5.0, 0.0, 4.0, 0.0, 9.0, 0.0, 0.0, 9.0],
[ 8.0, 8.0, 2.0, 0.0, 9.0, 4.0, 1.0, 4.0],
[10.0,10.0, 9.0, 8.0, 9.0,10.0, 6.0, 9.0],
[10.0,10.0, 4.0, 9.0,10.0, 4.0, 7.0, 7.0],
[ 7.0,10.0, 5.0, 5.0, 8.0, 5.0, 1.0,10.0],
[10.0,10.0, 9.0,10.0, 0.0,10.0, 7.0,10.0],
[ 8.0, 0.0, 4.0, 2.0, 5.0, 4.0, 1.0, 6.0],
[ 9.0, 7.0, 2.0, 4.0, 9.0, 0.0, 0.0, 4.0],
[10.0, 3.0, 8.0,10.0, 9.0,10.0,10.0, 7.0],
[10.0,10.0,10.0, 8.0,10.0, 9.0, 7.0, 9.0],
[10.0,10.0, 9.0,10.0,10.0,10.0,10.0,10.0]]

list_0 = list_grades[0]

length = len(list_0)

#for i in range(length):
    #print(list_0[i])

    #list_0[i]+= list_0[i] #adding to itself [14.0, 6.0, 14.0, 14.0, 18.0, 0.0, 0.0, 0.0]
    #new_list = list_0[i]
    #print(new_list)

print(list_0)
sumar = sum(list_0)
print(sumar)
    #calculate_grade = 

#%%

# problem b use sort
#(b) Compute the mean, median, and standard deviation of the class as a whole.
list_grades = [[ 7.0, 3.0, 7.0, 7.0, 9.0, 0.0, 0.0, 0.0],
[10.0,10.0, 8.0,10.0,10.0,10.0, 1.0,10.0],
[10.0, 0.0, 5.0,10.0, 9.0,10.0, 8.0, 8.0],
[10.0,10.0, 5.0, 2.0,10.0,10.0,10.0, 8.0],
[10.0,10.0, 8.0,10.0, 9.0, 9.0,10.0, 9.0],
[ 9.0, 7.0, 8.0, 7.0, 0.0, 6.0, 6.0, 6.0],
[ 5.0, 0.0, 5.0, 3.0, 2.0,10.0, 6.0, 0.0],
[ 9.0, 8.0, 8.0, 5.0, 7.0, 8.0, 5.0,10.0],
[10.0,10.0, 3.0,10.0, 9.0,10.0,10.0, 8.0],
[ 8.0, 5.0, 7.0, 5.0, 8.0, 8.0, 4.0, 8.0],
[ 8.0, 0.0, 9.0, 0.0, 8.0,10.0, 9.0,10.0],
[ 5.0, 0.0, 4.0, 0.0, 9.0, 0.0, 0.0, 9.0],
[ 8.0, 8.0, 2.0, 0.0, 9.0, 4.0, 1.0, 4.0],
[10.0,10.0, 9.0, 8.0, 9.0,10.0, 6.0, 9.0],
[10.0,10.0, 4.0, 9.0,10.0, 4.0, 7.0, 7.0],
[ 7.0,10.0, 5.0, 5.0, 8.0, 5.0, 1.0,10.0],
[10.0,10.0, 9.0,10.0, 0.0,10.0, 7.0,10.0],
[ 8.0, 0.0, 4.0, 2.0, 5.0, 4.0, 1.0, 6.0],
[ 9.0, 7.0, 2.0, 4.0, 9.0, 0.0, 0.0, 4.0],
[10.0, 3.0, 8.0,10.0, 9.0,10.0,10.0, 7.0],
[10.0,10.0,10.0, 8.0,10.0, 9.0, 7.0, 9.0],
[10.0,10.0, 9.0,10.0,10.0,10.0,10.0,10.0]]

for i in range(len(list_grades)):

    sumar = sum(list_grades[i])
    print(sumar)

total = sumar / len(list_grades)
print(total)

#%%
for item in ["rat", "bunny", "firu"]:
    valor = item
    print(item," ", valor)


#%%
