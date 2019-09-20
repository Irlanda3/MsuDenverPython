#%%
for item in 'Python':
    print(item)

#%%
for item in ["mosh", "rat", "conejo" ]:
    print(item)
type(["mosh", "rat", "conejo" ])
#%%
for item in ['mosh','bunny', 'conejo']:
    print(item)
type(['mosh','bunny', 'conejo'])
#%%
for item in range(10):
    print(item)#0-9


#%%
for item in range(5, 10):
    print(item)#5-9


#%%
for item in range(5, 10, 2):
    print(item)


#%%
prices = [10, 20, 30]
total = 0
for item in prices:
    #we get the current price and add it to the total

    total = total + item
    item += item
print(item)
print(f"Total: {total} ")


#%%
#NESTED LOOPS
for x in range(4):
    #for each  x we generate  numebres
    for y in range(3): #este loop termina primero y ya pasa al primer loop para iterar con otro numero diferente

        print(f'({x}, {y})')


#%%
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output+='x'
        print(range(x_count))
    print(output)



#%%
