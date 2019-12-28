import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
t = np.arange(0, 50, 0.05)
def deffer(z,t):
    s,v = z
    ds_dt = v
    dv_dt=-9.8*np.sin(s/l)-k/m*v
    return ds_dt, dv_dt
l = 10
m = 10
k = 1
s0 = 3
v0 = 0
z0=s0,v0
sol = odeint(deffer,z0,t)
plt.plot(t,sol[:,0])

plt.show()
    