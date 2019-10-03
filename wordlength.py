#%%
def longer_than(n, wordList):
    for i in wordList:#leemos la lista
        #print(i)
        #print(len(i))
        if len(i) < n: #y le pedimos que haga algo si cumple la cond
            #print(i,"iside if")
            wordList.remove(i)  
            print(len(wordList))
               
    return  print(wordList)
longer_than(3, ["only", "recursion", "brain","on"] )
longer_than(3, ["only", "recursion", "brain","on","the"] )
'''OUTPUT:
3
['only', 'recursion', 'brain']
4
['only', 'recursion', 'brain', 'the']
'OUTPUT:\n\n\n'

'''



#%%
