import sys
import random

list1=[1,2,3,4,5]
list2=[1,2,3,4,5]

a = random.choice(list1)
b = random.choice(list2)

print(a,"X",b)
u = int(input("Enter a number: "))

if u/a == b:
    print("you are rigth")
else:
    print("wrong")