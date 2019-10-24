#%% 
# importing the required module 
from matplotlib import pyplot as plt
  
# x axis values 
x = [1,2,3] 
# corresponding y axis values 
y = [2,4,1] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show()

# %%
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

# %%
#%%
from math import pi, sin, degrees
import math
# importing the required module 
import matplotlib.pyplot as plt

omega = (2*pi)/86164.09
print("Earth angular velocity: ", omega)
# f_coriolisParameter -> earth local rotatiom -> f = 2*omega*sin(phi_degrees)
phi_degrees = pi/6#30degrees
math.degrees(phi_degrees)
f = 2*omega*sin(phi_degrees)
math.degrees(f)
print("f_coriolis parameter: ", f) # we got a float
print(type(f))
dosTimesPi = 2*pi
geostrophic_adjustmentTime =  (0.25)*( (dosTimesPi) / f) 

print("Geostrophic Adjustment Time: ", geostrophic_adjustmentTime)
plt.title('Geostrophic Adjustment Time!')
plt.plot(geostrophic_adjustmentTime)

plt.show()

def gatFnc():
    return


# %%
