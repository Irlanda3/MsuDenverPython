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