#%%
'''aprenderemos lambda function. branching if then else
https://www.w3schools.com/python/python_lambda.asp
'''
g = lambda x,y: x+y
g(1,2)

#%%
f= lambda c: 9.0/5.0 * c + 32.0
f(23)

#%%
'''if then else
if condition:
    statement
    statement
else:
    statements
    statements
'''
def andrew(f):
    if f <= 40:
        print("It is freezing")
    else:
        print("it is toasty")
    return

andrew(f (23) )

#%%
x = [1, 2, 4.9, 9.7, -11]
if ( x[0] > 10 and x[1] < 11 and x[4] < 0 ):
    x[3] = 5

else:
    x[3] = 2.7


#%%
#aqui es boolean  por que me dice evalua si esto es verdar o mentira
#no me esta diciendo que haga una order
if ( x[0]!=0 and sum(x) < 500):
    cond_1 = (x[0] > 10)
print(cond_1)

#%%
'''
if condition:
    statement
    statement
elif condition
    statement
    statement
else
    statement

esto es como sun switch por que segun en python
no existe eso. estos elseif son como caso 1, caso 2, caso3 etc
    '''
s = ["Laura", "Andrew", "Aaron"]
for x in s:
    if x == "Laura":
        grade = 100
    elif x== "Andrew":
        grade = 72
    elif x== "Aaron":
        grade = 86
    else:
        grade = 41


#%%
#Inline if then else:
#value_1 if condition else value_2
y = 7 if (2 > 1) else 8


#%%
#lab 6
'''A  90.0-100%B  
80.0-89.9%C  70.0-79.9%D  60.0-69.9%F  below 60.0%
lo que queremos es la suma de cada [] y luego el average y ya
luego queremos saber que saco si una a o b
'''

grades = [[ 7.0, 3.0, 7.0, 7.0, 9.0, 0.0, 0.0, 0.0],
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
[10.0,10.0, 4.0, 9.0,10.0, 4.0, 7.0, 7.0],[ 7.0,10.0, 5.0, 5.0, 8.0, 5.0, 1.0,10.0],[10.0,10.0, 9.0,10.0, 0.0,10.0, 7.0,10.0],[ 8.0, 0.0, 4.0, 2.0, 5.0, 4.0, 1.0, 6.0],[ 9.0, 7.0, 2.0, 4.0, 9.0, 0.0, 0.0, 4.0],[10.0, 3.0, 8.0,10.0, 9.0,10.0,10.0, 7.0],[10.0,10.0,10.0, 8.0,10.0, 9.0, 7.0, 9.0],[10.0,10.0, 9.0,10.0,10.0,10.0,10.0,10.0]]
'''aqui necesitamos sumar cada lista y dividirlo por 80
luego necesitamoss hacer un porcentaje de lo que nos dio
'''
for x in grades:
    #print(x)
    if sum(x) >= 90:
        grade = "A"
        print(x, "grades a")
        print(grade)
        total = sum(x)/8
        print(total)
    elif sum(x) >= 8.0 and sum(x) <9.0:
        grade = "B"
        print(x, "grades b")
        print(grade)
        total = sum(x)/8
        print(total)
    elif sum(x) >= 7.0 and sum(x) < 8.0:
        grade = "C"
        print(grade)
        print(x, "grades c")
        total = sum(x)/8
        print(total)
    #elif sum(x) >= 60 and sum(x) < 70:
     #   grade = "D"
    else:
        sum(x)
        grade = 41
        total = sum(x)/8
        print(total)

    #print(grade)

#%%
grades = [[ 7.0, 3.0, 7.0, 7.0, 9.0, 0.0, 0.0, 0.0],
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
[10.0,10.0, 4.0, 9.0,10.0, 4.0, 7.0, 7.0],[ 7.0,10.0, 5.0, 5.0, 8.0, 5.0, 1.0,10.0],[10.0,10.0, 9.0,10.0, 0.0,10.0, 7.0,10.0],[ 8.0, 0.0, 4.0, 2.0, 5.0, 4.0, 1.0, 6.0],[ 9.0, 7.0, 2.0, 4.0, 9.0, 0.0, 0.0, 4.0],[10.0, 3.0, 8.0,10.0, 9.0,10.0,10.0, 7.0],[10.0,10.0,10.0, 8.0,10.0, 9.0, 7.0, 9.0],[10.0,10.0, 9.0,10.0,10.0,10.0,10.0,10.0]]
'''aqui necesitamos sumar cada lista y dividirlo por 80
luego necesitamoss hacer un porcentaje de lo que nos dio
'''
for x in grades:
    
    if sum(x) >= 90:
        grade = "A"
        print(x)
        print(sum(x))
        #total = sum(x)/80
        print(total)
    




#%%
