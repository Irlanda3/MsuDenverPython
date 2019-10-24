# %%
from math import pi, sin, degrees
import math
# importing the required module
import matplotlib.pyplot as plt


def gatFnc(phi_degrees):
    omega = (2*pi)/86164.09


    print("Earth angular velocity: ", omega)
    # f_coriolisParameter -> earth local rotatiom -> f = 2*omega*sin(phi_degrees)
    #phi_degrees = pi/6  # 30degrees
    math.degrees(phi_degrees)
    f = 2*omega*sin(phi_degrees)
    math.degrees(f)
    print("f_coriolis parameter: ", f)  # we got a float
    print(type(f))
    dosTimesPi = 2*pi
    geostrophic_adjustmentTime = (0.25)*((dosTimesPi) / f)

    print("Geostrophic Adjustment Time: ", geostrophic_adjustmentTime)
    

    return geostrophic_adjustmentTime

plt.plot(gatFnc(pi/6), 'g^')
plt.ylabel("GAT")
plt.show()

# gatFnc(pi/6)
# gatFnc(7*pi/36)
# name = ['30deg']
# plt.title('Geostrophic Adjustment Time!')

# plt.plot(gatFnc(pi/6),name)
# plt.show()

# the histogram of the data
# n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

# %%
