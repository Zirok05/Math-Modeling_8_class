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


