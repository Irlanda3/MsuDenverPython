#%%
e = [2, 4, 6, 8]
o = [1, 3, 5, 7, 9]
c = [0, 10]
# Example: Create the list [1, 4, 6]
lst_1 = [o[0]] + e[1:3]
print(lst_1)

# Create the list [0, 1, 5, 9, 10]
lst_2 = [c[0]] + o[0::2] + [c[1]]
print(lst_2)

# Create the list [2, 6, 9, 5, 1]
lst_3 = e[0::2] + o[-1::-2]
print(lst_3)

'''
OUTPUT
[1, 4, 6]
[0, 1, 5, 9, 10]
[2, 6, 9, 5, 1]

'''

#%%
