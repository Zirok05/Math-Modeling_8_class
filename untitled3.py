import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig=plt.figure()

x = np.linspace(-5, 5, 100)
a =10
b =20
c =5
y = a*x**2 + b*x + c
anim_list = []
for i in range(0,100,1):
    anim_object, = plt.plot(x[i], y[i],'o',color='r')
    anim_list.append([anim_object])
ani=ArtistAnimation(fig,anim_list,interval = 50)
ani.save('ani.gif')
