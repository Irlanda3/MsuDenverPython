
# random gives me a float, randint gives a integer

from random import randint, random
x = random()
p = randint(2, 16)

print("{x:7.5f}".format(x=x))


from random import randint, random
x = random()
p = randint(2,16)
fstr = "{{x:{}.{}f}}".format(p+2,p)

print(fstr.format(x=x))