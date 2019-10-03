#%%
def most_vowels(wordlist):
    vowel = set("aeiouAEIOU")
    #str1 = ''.join(wordlist)
    
    count = 0
    for i in wordlist:
        
        if i in vowel: #if buddy in vowels                     
            print(i)

            count += wordlist.count(i)
                       
    return count

print(most_vowels(["Buddy", "Oreo", "Max", "Toto"]) )
#necesito funcion que separe los palabras en una lista

#%%
def vowel_count(str): 
      
    # Intializing count variable to 0 
    count = 0
      
    # Creating a set of vowels 
    vowel = set("aeiouAEIOU") 
      
    # Loop to traverse the alphabet 
    # in the given string 
    for alphabet in str: 
      
        # If alphabet is present 
        # in set vowel 
        if alphabet in vowel: 
            count = count + 1
            print("No. of vowels :", count) 
      
# Driver code  
#str = "GeeksforGeeks"
str = ["Buddy", "Oreo", "Max", "Toto"]  
# Function Call 
vowel_count(str) 

#%%
from re import search
lista = ["Buddy", "Oreo", "Max", "Toto"]
w = []
for word in lista:#por cada palabra en la lista
    counter = 0
    counta = 0; counte=0; counti=0; counto=0; countu=0
    #print(i)
    for vocales in word:#for j in each word iterate the word
        #print(vocales)
        if search("a", vocales):  
            counter += 1
            counta+=1
        elif search("e",vocales):
            counter += 1
            counte+=1
        elif search("i",vocales):
            counter += 1
            counti+=1
        elif search("o",vocales):
            counter += 1
            counto+=1
        elif search("u",vocales):
            counter += 1
            countu+=1
    w.append(counter)#pon el numero de veces que se encontro en un list
print(lista[w.index(max(w))])#max encuntra el numero mas grande y regresa ese index
print(w)
   
        



#%%


#%%
