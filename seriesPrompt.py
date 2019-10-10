# %%
from __future__ import division
import math
n = int(input())
count1 = 0
for i in range(1, n+1):
    print(i) 
    count1 += (1 / i)
    print(1,"/",i)
    print("this is count1 result from division: ", count1)  
       
print("result outside loop", count1)
logaritmo_natural = math.log(n)
result = count1 - logaritmo_natural
print("FINAL ANSWER", result)

'''OUTPUT:
PS C:\Users\anayeli\Documents\PythonScientificProgramming> python seriesPrompt.py
5
1
(1, '/', 1)
('this is count1 result from division: ', 1.0)
2
(1, '/', 2)
('this is count1 result from division: ', 1.5)
3
(1, '/', 3)
('this is count1 result from division: ', 1.8333333333333333)
4
(1, '/', 4)
('this is count1 result from division: ', 2.083333333333333)
5
(1, '/', 5)
('this is count1 result from division: ', 2.283333333333333)
('result outside loop', 2.283333333333333)
('FINAL ANSWER', 0.6738954208992329)'''


