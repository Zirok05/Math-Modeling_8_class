import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation
seconds_in_year = 365*24*60*60
seconds_in_day = 24*60*60
years = 1.5
t = np.arange(0,2*seconds_in_day,60)

def PPC(s,t):
    (x1,v_x1,y1,v_y1,
     x2,v_x2,y2,v_y2,
     x3,v_x3,y3,v_y3) = s
     
    dxdt1 = v_x1
    dv_xdt1 = -G * m2 * (x1-x2) / ((x1-x2)**2 + (y1-y2)**2)**1.5
    dydt1 = v_y1
    dv_ydt1 = -G * m2 * (y1-y2) / ((x1-x2)**2 + (y1-y2)**2)**1.5
    
      
    dxdt2 = v_x2
    dv_xdt2 = -G * m1 * (x2-x1) / ((x2-x1)**2 + (y2-y1)**2)**1.5
    dydt2 = v_y2
    dv_ydt2 = -G * m1 * (y2-y1) / ((x2-x1)**2 + (y2-y1)**2)**1.5
    
    dxdt3 = v_x3
    dv_xdt3 = -G * m1 * (x3-x1) / ((x3-x1)**2 + (y3-y1)**2)**1.5
    dydt3 = v_y3
    dv_ydt3 = -G * m1 * (y3-y1) / ((x3-x1)**2 + (y3-y1)**2)**1.5
    
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2 ,dv_xdt2, dydt2, dv_ydt2,
            dxdt3 ,dv_xdt3, dydt3, dv_ydt3)
    
radius1 = 6371000
radius2 = 1731000
radius3 = 6371000/2
x10 = 384400000
v_x10 = 0  
y10 = 0
v_y10 = 0 

x20 = 0
v_x20 = 0
y20 = 0
v_y20 = 0 
   
x30 = 384400000/2
v_x30 = 0
y30 = 0
v_y30 = 0 

s0 = (x10,v_x10,y10,v_y10,
      x20,v_x20,y20,v_y20,
      x30,v_x30,y30,v_y30)

G = 6.67 * 10**(-11)
m1 = 5.972E24
m2 = 7.34767309*10**22
m3 = 5.972E24/2
move_array = np.ndarray(shape=(len(t), 6))
for i in range(0,len(t)-1, 1):
    
    tau = [t[i], t[i+1]]
    
    sol = odeint(PPC,s0,tau)
    
    move_array[i, 0] = sol[1,0]
    move_array[i, 1] = sol[1,2]
    move_array[i, 2] = sol[1,4]
    move_array[i, 3] = sol[1,6]
    move_array[i, 2] = sol[1,8]
    move_array[i, 3] = sol[1,10]
    
    
    x10 = sol[1,0]
    v_x10 = sol[1,1] 
    y10 = sol[1,2]
    v_y10 = sol[1,3]
    x20 = sol[1,4]
    v_x20 = sol[1,5]
    y20 = sol[1,6]
    v_y20 = sol[1,7]
    x30 = sol[1,8]
    v_x30 = sol[1,9]
    y30 = sol[1,10]
    v_y30 = sol[1,11]

    r12 = np.sqrt((x10-x20-x30)**2 + (y10-y20-y30)**2)

    if r12 <= radius1+radius2:
        V_x10 = (2 * m2 * v_x20 + v_x10 * (m1-m2)) / (m1 +m2)
        V_x20 = (2 * m1 * v_x10 + v_x20 * (m2-m1)) / (m1 +m2)
        V_x30 = (2 * m2 * v_x20 + v_x30 * (m3-m2)) / (m3 +m2)
    else:
        V_x10 = v_x10
        V_x20 = v_x20
        V_x30 = v_x30
    s0 = (x10,V_x10,y10,v_y10,
          x20,V_x20,y20,v_y20,
          x30,V_x30,y30,v_y30)
fig = plt.figure()
bodys =[]


for i in range(0, len(t), 1):
    
    body1, = plt.plot(move_array[i, 0], move_array[i,1], 'o',color='r', ms=20)
    body2, = plt.plot(move_array[i, 2], move_array[i,3], 'o',color='g', ms=20)
    body3, = plt.plot(move_array[i, 4], move_array[i,5 ], 'o',color='b', ms=20)
    bodys.append([body1,body2,body3])
    
ani = ArtistAnimation(fig,bodys,interval = 1)
plt.axis('equal')
ani.save('balll.gif')