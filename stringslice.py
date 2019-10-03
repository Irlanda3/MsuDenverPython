#%%
m = "metropolitan"
s = "state"
u = "university"
d = "denver"
a = "awesome"
b = "believe"
# Example: Create the string "bouwmeester"
str_1 = b[0] + a[4] + u[0] + a[1] + m[0:2] + u[4:9:2] + d[-2:]
print(str_1)

# Create the string "roadrunner"
str_2 = m[3:5] + m[-2] + d[0:6:5] + u[0] + u[1] + u[1]+d[4:6]
print(str_2)

# Create the string "emotion"
str_3 = m[-11::-1] + a[4] +u[-2:-9:-6] + m[6:12:5]

print(str_3)

'''
bouwmeester
roadrunner
emotion
'''

#%%
