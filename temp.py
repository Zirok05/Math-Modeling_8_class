import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
t = np.arange(10**(-7), 1.5*10**(-7), 10**(-9))
a = 0.008
v = 4*10**6
k = 9*10**9
def GG(s, t):  
    (x1, v_x1, y1, v_y1,
    x2, v_x2, y2, v_y2,
    x3, v_x3, y3, v_y3,
    x4, v_x4, y4, v_y4) = s
    dxdt1= v_x1
    dv_xdt1 = k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
    + k * q1 * q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5 
    + k * q1 * q4 / m1 * (x1 - x4) / ((x1 - x4)**2 + (y1 - y4)**2)**1.5
    
    dydt1 = v_y1
    dv_ydt1 = k * q1 * q2 / m1 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
    + k * q1 * q3 / m1 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5 
    + k * q1 * q4 / m1 * (y1 - y4) / ((x1 - x4)**2 + (y1 - y4)**2)**1.5
    
    
     
    dxdt2 = v_x2
    dv_xdt2 = k * q2 * q1 / m2 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
    + k * q2 * q3 / m2 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5 
    + k * q2 * q4 / m2 * (x2 - x4) / ((x2 - x4)**2 + (y2 - y4)**2)**1.5
    
    dydt2 = v_y2
    dv_ydt2 = k * q2 * q1 / m2 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
    + k * q2 * q3 / m2 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5 
    + k * q2 * q4 / m2 * (y2 - y4) / ((x2 - x4)**2 + (y2 - y4)**2)**1.5
    
    
    dxdt3= v_x3
    dv_xdt3 = k * q3 * q1 / m3 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
    + k * q3 * q2 / m3 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5 
    + k * q3 * q4 / m3 * (x3 - x4) / ((x3 - x4)**2 + (y3 - y4)**2)**1.5
    
    dydt3= v_y3
    dv_ydt3 = k * q3 * q1 / m3 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
    + k * q3 * q2 / m3 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5 
    + k * q3 * q4 / m3 * (y3 - y4) / ((x3 - x4)**2 + (y3 - y4)**2)**1.5
    
    
    dxdt4= v_x4
    dv_xdt4 = k * q4 * q1 / m4 * (x4 - x1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
    + k * q4 * q2 / m4 * (x4 - x2) / ((x4 - x2)**2 + (y4 - y2)**2)**1.5 
    + k * q4 * q3 / m4 * (x4 - x3) / ((x4 - x3)**2 + (y4 - y3)**2)**1.5
    
    dydt4= v_y4
    dv_ydt4 = k * q4 * q2 / m4 * (y4 - y2) / ((x4 - x2)**2 + (y4 - y2)**2)**1.5
    + k * q4 * q3 / m4 * (y4 - y3) / ((x4 - x3)**2 + (y4 - y3)**2)**1.5 
    + k * q4 * q1 / m4 * (y4 - y1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
    
    
    return(dxdt1,dv_xdt1,dydt1,dv_ydt1,
           dxdt2,dv_xdt2,dydt2,dv_ydt2,
           dxdt3,dv_xdt3,dydt3,dv_ydt3,
            dxdt4,dv_xdt4,dydt4,dv_ydt4)
    
    
x01 = -a
v_x01 = -v/2**0.5
y01 = a
v_y01 = -v/2**0.5
    
x02 = a
v_x02 = -v/2**0.5
y02 = a
v_y02 = v/2**0.5
    
x03 = a
v_x03 = v/2**0.5 
y03 = -a
v_y03 = v/2**0.5
    
x04 = -a
v_x04 = v/2**0.5
y04 = -a
v_y04 = -v/2**0.5

s0 = (x01,v_x01,y01,v_y01,
      x02,v_x02,y02,v_y02,
      x03,v_x01,y03,v_y03,
      x04,v_x04,y04,v_y04)

m1 = 1.1*10**(-27)
q1 = 1.1*10**(-13)

m2 = 1.1*10**(-27)
q2 = 1.1*10**(-13)

m3 = 1.1*10**(-27)
q3 = 1.1*10**(-13)

m4 = 1.1*10**(-27)
q4 = 1.1*10**(-13)

sol = odeint(GG,s0,t)

fig = plt.figure()
bodys =[]

for i in range(0,len(t),1):
    body1, = plt.plot(sol[:i,0],sol[:i,2],'-',color='r')
    body1_line, = plt.plot(sol[i,0],sol[i,2],'o',color='r')
    
    body2, = plt.plot(sol[:i,4],sol[:i,6],'-',color='g')
    body2_line, = plt.plot(sol[i,4],sol[i,6],'o',color='g')
    
    body3, = plt.plot(sol[:i,8],sol[:i,10],'-',color='b')
    body3_line, = plt.plot(sol[i,8],sol[i,10],'o',color='b')
    
    body4, = plt.plot(sol[:i,12],sol[:i,14],'-',color='yellow')
    body4_line, = plt.plot(sol[i,12],sol[i,14],'o',color='yellow')
    
    bodys.append([body1, body1_line,body2, body2_line,body3, body3_line,body4, body4_line])
    
ani = ArtistAnimation(fig,bodys,interval=50)
plt.axis('equal')
ani.save('GG.gif')    

    
    
    
    
    
    
    
    
    
    
    
    
    