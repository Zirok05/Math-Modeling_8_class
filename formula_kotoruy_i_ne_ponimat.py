

from constant import g,M,R,h2,k
from math import pi,sqrt,e
h=100
v = sqrt(g*h*pi/(2*M*R))
print(v)
t=200
n = (2/sqrt(pi)*h2/(k*t))*e**(-300/k*t)*300**(t/2)
print(n)
