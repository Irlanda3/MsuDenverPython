#%%
''' 1.4
Exercise 1.4: Convert from meters to British length units
Make a program where you set a length given in meters and then compute and write
out the corresponding length measured in inches, in feet, in yards, and in miles. Use
that one inch is 2.54 cm, one foot is 12 inches, one yard is 3 feet, and one British
mile is 1760 yards. For verification, a length of 640 meters corresponds to 25196.85
inches, 2099.74 feet, 699.91 yards, or 0.3977 miles.
Filename: length_conversion.'''

#val = raw_input("enter a number in meters: ")
#print(val)


length_in_meters = 640
inches = 39.37*length_in_meters
feet = 3.28*length_in_meters
yards = 1.0936*length_in_meters
miles = 0.0006*length_in_meters

print("640 meters is equal to the following British units")
print(inches," inches")
print(feet, " feet")
print(yards," yards")
print(miles, "miles")

'''RESULTS:
640 meters is equal to the following British units
25196.8  inches
2099.2  feet
699.904  yards
0.38399999999999995 miles'''
