import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

def circle_func(x_centre, y_centre, R, N):
    x = np.zeros(N)
    y = np.zeros(N)
    for i in range(N):
        alpha = np.linspace(0, 2*np.pi, N)
        x[i] = x_centre + R*np.cos(alpha[i])
        y[i] = y_centre + R*np.sin(alpha[i])
    return x, y

N = 100
R = 4

fig = plt.figure()
anim_list = []
thetas = np.linspace(0.4*np.pi, N)
x_centre_move = R * thetas
y_centre_move = 3 
ostroid_x = R * np.cos(thetas)**3
ostroid_y = R * np.sin(thetas)**3
#----------------------------------------main----------------------------------------
for i in range(N):
    x, y = circle_func(x_centre_move[i], y_centre_move[i], R, N)
    circle, = plt.plot(x, y)
    anim_object, = plt.plot(x_centre_move[:i], y_centre_move[:i], 'o')
    anim_list.append([circle, anim_object])
#----------------------------------------main----------------------------------------
plt.axis('equal')
ani = ArtistAnimation(fig, anim_list, interval = 50)
ani.save('lol.gif')