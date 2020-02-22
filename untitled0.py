import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

N = 100
alpha = np.linspace(0, 10 ,N)
x = np.cos(alpha)
y = np.sin(alpha)
z = alpha * 0.1

ball, = ax.plot(x,y,z,'o',color='g')
line, = ax.plot(x,y,z,'-',color='r')

def GG(i):
    ball.set_data(x[i],y[i])
    ball.set_3d_properties(z[i])
    
    line.set_data(x[:i],y[:i])
    line.set_3d_properties(z[:i])
    
ax.set_xlim3d([-1.0,1.0])
ax.set_xlabel('X')

ax.set_ylim3d([-1.0,1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-1.0,1.0])
ax.set_zlabel('Z')
    
ani = animation.FuncAnimation(fig,GG,N,interval = 50)
ani.save('fhgft.gif')