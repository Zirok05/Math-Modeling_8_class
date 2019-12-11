def circle_f(x_centre,y_centre, R, N):
    x=np.zeros(N)
    y=np.zeros(N)
    for i in range(N):
        alpha=np.linspace(0,2*np.pi,100)
        x[i]=x_centre+R*np.cos(alpha[i])
        y[i]=y_centre+R*np.sin(alpha[i])
    return x,y