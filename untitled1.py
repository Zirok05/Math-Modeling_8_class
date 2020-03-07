import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
t = np.arange(10**(-7), 1.5*10**(-7), 10**(-9))
x0 = 0
y0 = 0
def PPC(r,N,v):
    for i in range(0,N,1):
        al = 2*np.pi/N
        x = np.sin(al*i)*r
        y = np.cos(al*i)*r
        if x<0 and y<0: 
            vx=v*np.sin(0.5*np.pi-al*i)
            vy=-v*np.cos(0.5*np.pi-al*i)
        elif x<0 and y>0:
            vx=v*np.cos(al*i)
            vy=-v*np.sin(al*i)
        elif x>=0 and y>=0:
            vx=-v*np.cos(np.pi+al*i)
            vy=v*np.sin(np.pi+al*i)
        elif x>0 and y<0:
            vx=v*np.cos(-al*i)
            vy=v*np.sin(-al*i)
        else:
            vx=0
            vy=0
        print(x, vx, y, vy)
#        plt.plot(0,0,marker='o')
#        plt.arrow(x,y,vx,vy)
#        plt.scatter(x,y)        
#        plt.plot(x,y,marker='o')
#    plt.axis("equal")
#    plt.show()
v = (6.67 * 10**(-11) * 1.9 * 10**30 / (149 * 10**9))**0.5
print()
PPC(149 * 10**9, 50, v )  