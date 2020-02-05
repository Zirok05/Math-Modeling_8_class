import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

seconds_in_year = 365*24*60*60
seconds_in_day  = 24*60*60
years = 2

t = np.arange(0,years*seconds_in_year,seconds_in_day)

def PPC(z,t):
    
    (x_neptun,v_x_neptun, y_neptun,v_y_neptun,
    x_plyton,v_x_plyton,y_plyton,v_y_plyton) = z
     
    dxdt_neptun = v_x_neptun
    dv_xdt_neptun = -G * sun_mass * x_neptun / (x_neptun**2 + y_neptun**2)**1.5
    dydt_neptun = v_y_neptun
    dv_ydt_neptun = -G * sun_mass * y_neptun / (x_neptun**2 + y_neptun**2)**1.5
    
    dxdt_plyton = v_x_plyton
    dv_xdt_plyton = -G * sun_mass * x_plyton /(x_plyton**2 + y_plyton**2)**1.5
    dydt_plyton = v_y_plyton
    dv_ydt_plyton = -G + sun_mass *y_plyton /(x_plyton**2 + y_plyton**2)**1.5
    
    return (dxdt_neptun,dv_xdt_neptun,dydt_neptun,dv_ydt_neptun,
             dxdt_plyton, dv_xdt_plyton,dydt_plyton,dv_ydt_plyton)
    
x0_neptun = 4503443661000
v_x0_neptun =  0
y0_neptun = 0
v_y0_neptun = 5434.9

x0_plyton = 5868000000000
v_x0_plyton = 0
y0_plyton = 0
v_y0_plyton =  4669.1

z0 = (x0_neptun,v_x0_neptun,y0_neptun,v_y0_neptun,
      x0_plyton,v_x0_plyton,y0_plyton,v_y0_plyton)

G = 6.67 * 10**(-11)
sun_mass = 1.9 * 10**30

sol = odeint(PPC,z0,t)

fig = plt.figure()
planets = []

for i in range(0, len(t), 1):
    
    sun, = plt.plot([0], [0], 'yo', ms=10)
    
    neptun, = plt.plot(sol[:i, 0], sol[:i,2], 'r-')
    neptun_line, = plt.plot(sol[i,0], sol[i,2], 'ro')
    
    plyton, = plt.plot(sol[:i,4], sol[:i,6], 'b-')
    plyton_line, = plt.plot(sol[i,4], sol[i,6], 'bo')
    
    planets.append([sun,neptun,neptun_line,plyton,plyton_line])
    
ani = ArtistAnimation(fig,planets,interval = 50)
plt.axis('equal')
ani.save('neptun_plyton.gif')








#
