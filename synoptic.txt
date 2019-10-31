# %%
from math import pi, sin, degrees
import math
# importing the required module
import matplotlib.pyplot as plt


def gatFnc(phi_degrees):
    omega = (360)/86164
    print("Earth angular velocity: ", omega)
    # f_coriolisParameter -> earth local rotatiom -> f = 2*omega*sin(phi_degrees)
    #phi_degrees = pi/6  # 30degrees
    math.degrees(phi_degrees)
    f = 2*omega*sin(phi_degrees)
    math.degrees(f)
    fTOhrs = f*3600
    print("f_coriolis parameter: ", fTOhrs)  # we got a float    
    dosTimesPi = 360
    geostrophic_adjustmentTime = (0.25)*((dosTimesPi) / fTOhrs)
    print("Geostrophic Adjustment Time: ", geostrophic_adjustmentTime)
    print("")

    return geostrophic_adjustmentTime

degreeName = [30,35,40,45,50,55,60]

gatList = []
gatList = (gatFnc(pi/6),gatFnc(7*pi/36),gatFnc(2*pi/9),gatFnc(pi/4),gatFnc(5*pi/18),gatFnc(11*pi/36),gatFnc(pi/3))
plt.plot(gatList, 'g^')#talves sea buena idea poner en una lista todos los resultados del gat

plt.ylabel("GAT Time In Hrs")
plt.xlabel("LATITUDES")

plt.xticks([0, 1,2,3,4, 5,6], ('x = 30','x = 35','x = 40','x = 45','x = 50','x = 55','x = 60'))
#plt.tight_layout()

plt.title("Geostrophic Adjustment Time")
plt.grid(True)
plt.show()

# %%
from math import pi, sin, degrees
import math
# importing the required module
import matplotlib.pyplot as plt


def gatFnc(phi_degrees):
    omega = (360)/38400
    print("Saturn angular velocity: ", omega)
    # f_coriolisParameter -> earth local rotatiom -> f = 2*omega*sin(phi_degrees)
    #phi_degrees = pi/6  # 30degrees
    math.degrees(phi_degrees)
    f = 2*omega*sin(phi_degrees)
    math.degrees(f)
    fTOhrs = f*3600
    print("f_coriolis parameter: ", fTOhrs)  # we got a float    
    dosTimesPi = 360
    geostrophic_adjustmentTime = (0.25)*((dosTimesPi) / fTOhrs)
    print("Geostrophic Adjustment Time: ", geostrophic_adjustmentTime)
    print("")

    return geostrophic_adjustmentTime

degreeName = [30,35,40,45,50,55,60]

gatList = []
gatList = (gatFnc(pi/6),gatFnc(7*pi/36),gatFnc(2*pi/9),gatFnc(pi/4),gatFnc(5*pi/18),gatFnc(11*pi/36),gatFnc(pi/3))
plt.plot(gatList, 'g^')#talves sea buena idea poner en una lista todos los resultados del gat

plt.ylabel("GAT Time In Hrs")
plt.xlabel("LATITUDES")

plt.xticks([0, 1,2,3,4, 5,6], ('x = 30','x = 35','x = 40','x = 45','x = 50','x = 55','x = 60'))
#plt.tight_layout()

plt.title("Geostrophic Adjustment Time")
plt.grid(True)
plt.show()

# %%
from math import pi, sin, degrees
import math
# importing the required module
import matplotlib.pyplot as plt


def gatFnc(phi_degrees):
    omega = (360)/5067030
    print("Mercury angular velocity: ", omega)
    # f_coriolisParameter -> earth local rotatiom -> f = 2*omega*sin(phi_degrees)
    #phi_degrees = pi/6  # 30degrees
    math.degrees(phi_degrees)
    f = 2*omega*sin(phi_degrees)
    math.degrees(f)
    fTOhrs = f*3600
    print("f_coriolis parameter: ", fTOhrs)  # we got a float    
    dosTimesPi = 360
    geostrophic_adjustmentTime = (0.25)*((dosTimesPi) / fTOhrs)
    print("Geostrophic Adjustment Time: ", geostrophic_adjustmentTime)
    print("")

    return geostrophic_adjustmentTime

degreeName = [30,35,40,45,50,55,60]

gatList = []
gatList = (gatFnc(pi/6),gatFnc(7*pi/36),gatFnc(2*pi/9),gatFnc(pi/4),gatFnc(5*pi/18),gatFnc(11*pi/36),gatFnc(pi/3))
plt.plot(gatList, 'g^')#talves sea buena idea poner en una lista todos los resultados del gat

plt.ylabel("GAT Time In Hrs")
plt.xlabel("LATITUDES")

plt.xticks([0, 1,2,3,4, 5,6], ('x = 30','x = 35','x = 40','x = 45','x = 50','x = 55','x = 60'))
#plt.tight_layout()

plt.title("Geostrophic Adjustment Time")
plt.grid(True)
plt.show()

# %%
