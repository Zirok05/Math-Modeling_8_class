import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0,50,0.01)
a = 8
b = 5
c = 15
d = 10
def Fiasko(z,t):
    theta,omega = z
    dtheta_dt = (a-b*omega)*theta
    domega_dt = (-c + d*theta)*omega
    return dtheta_dt, domega_dt
theta0 = 10
omega0 = 8
z0 = theta0, omega0
sol = odeint(Fiasko,z0,t)
plt.plot(sol[:,1], sol[:,0])

plt.show()
