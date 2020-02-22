import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np
#
#fig = plt.figure()
#ax = p3.Axes3D(fig)
#
#phi = np.linspace(0,2*np.pi, 100)
#theta = np.linspace(0, 2*np.pi,100)
#x = 2 * np.outer(phi, np.cos(theta))
#y = np.outer(phi,np.sin(theta))
#z = np.outer(phi**2,np.ones(np.size(theta)))
#
#ax.plot_surface(x,y,z,color='g')
#plt.show()
#
#
#
#
#
fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(-2*np.pi,2*np.pi, 100)
theta = np.linspace(-2*np.pi, 2*np.pi,100)
a = 1
b = 1.5
c = 3
x = np.outer(np.cos(phi),np.sinh(theta))
y = np.outer(np.sin(phi),np.sinh(theta))
z = np.outer(np.ones(np.size(phi)),np.sinh(theta))

ax.plot_surface(x,y,z,color='b')
plt.show()




fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0,2*np.pi, 100)
theta = np.linspace(0, 8*np.pi,100)
h = 10
x = np.outer(phi, np.cos(theta))
y = np.outer(phi,np.sin(theta))
z = np.outer(np.ones(np.size(phi)),h*theta)

ax.plot_surface(x,y,z,color='r')
plt.show()




fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0,2*np.pi, 100)
theta = np.linspace(0, 2*np.pi,100)
n = 1
l = 1
m = 1
x = np.outer(phi, np.cos(theta)) + l*np.outer(np.ones(np.size(phi)),  theta**0.5)
y = np.outer(phi,np.sin(theta)) + m*np.outer(np.ones(np.size(phi)), theta**0.5)
z = n*np.outer(np.ones(np.size(phi)),  theta**0.5)

ax.plot_surface(x,y,z,color='yellow')
plt.show()