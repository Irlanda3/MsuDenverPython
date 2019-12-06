'''chapter 6 practice examples '''
temps = [13, 15.4, 17.5]
print(type(temps))

temps2 = {'Oslo': 13, 'London': 15.4, 'Paris': 17.5}
print(type(temps2))
print(temps2)

temps3 = dict(Oslo=13, London=15.4, Paris=17.5)
print(type(temps3))
print(temps3)

temps2['Madrid'] = 26.0
temps2['irlanda'] = 30.0
print(temps2)

#dictionary operations

for city in temps2:
    print ("The temperature in %s is %g" %(city, temps2[city]))

if 'irlanda' in temps2:
    print('irlanda:', temps2['irlanda'])
else:
    print("No temperature data for irlanda")

'Oslo' in temps2

#temps3
temps3.keys()
temps3.values()

for city in sorted(temps3):#sorted in alphabetic order
    print(city)

del temps3['Oslo']
temps3
#%%
temps = {'Oslo': 13, 'London': 15.4, 'Paris': 17.5}
print(type(temps))
print(temps)
temps.keys()

temps.values()

for city in sorted(temps):
    print(city)

del temps['Oslo']
temps

len(temps)

temps_copy = temps.copy()
del temps_copy['Paris']

print('temps copy paris borrado')
temps

temps_copy
# %%
t1 = temps
ti['Stockholm'] = 10.0
temps

# %%
