#%%
def decide (temp):
    """ 3Print a decision based on an input temperature 
    in Fahrenheit4
    """
    if temp > 80:
        print("The temperature is",temp, " so we will go to Denver.")
    if temp > 55 and temp <= 80:
        print("The temperature is",temp, "so we will go to Steamboat Springs.")
    if temp > 40 and temp <= 55:
        print("The temperature is",temp, "so we will go to Breckenridge.")
    if temp > 32 and temp <= 40:
        print("The temperature is",temp, "so we will go to Avon.")
    if temp <= 32:
        print("The temperature is", temp, "so we will stay in.")
                
decide(85)
decide(60)
decide(45)
decide(36)
decide(10)

'''OUTPUT:
The temperature is 85  so we will go to Denver.
The temperature is 60 so we will go to Steamboat Springs.
The temperature is 45 so we will go to Breckenridge.
The temperature is 36 so we will go to Avon.
The temperature is 10 so we will stay in.
'''

#%%
