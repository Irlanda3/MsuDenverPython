# %%
import sys
import random

print("Let’s play a game!")
print("At anytime, to quit simply provide ’q’ for your answer.")
list1 = [5,6,7,8,9,10,11,12]
list2 = [5,6,7,8,9,10,11,12]
azar1 = random.choice(list1)
azar2 = random.choice(list2)

print(azar1," X ", azar2,"=")
print("Enter you answer")
answerByUser = int(input())


if answerByUser/azar1 == azar2:
    print("you are right")
else:
    print("you are wrong")

'''THIS PROGRAM WORKS, BUT i AM GETTING A WEIRD MESSAGE 
IN THE TERMINAL:
PS C:\Users\anayeli\Documents\PythonScientificProgramming> python multGame.py
  File "multGame.py", line 5
SyntaxError: Non-ASCII character '\xe2' in file multGame.py on line 5, but no encoding declared; 
see http://python.org/dev/peps/pep-0263/ for details'''
    
