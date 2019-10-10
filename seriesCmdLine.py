# %%
from __future__ import division
import math
import sys

n = int(sys.argv[1])
#n = int(input())
count1 = 0
for i in range(1, n+1):

    count1 += (1 / i)


logaritmo_natural = math.log(n)
result = count1 - logaritmo_natural
print("FINAL ANSWER", result)
'''OUTPUT:
PS C:\Users\anayeli\Documents\PythonScientificProgramming> python seriesCmdLine.py 5
('FINAL ANSWER', 0.6738954208992329)
'''
