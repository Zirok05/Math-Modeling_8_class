def ditch(m_ast,v_stolk):
    
    c=4200
    m=1.4*10**21
    t1=15
    k=(m_ast*v_stolk**2)/2
    t2=k/c/m+t1
    t3=t2-t1
    print(t3)
    if t3>50 and t3<100:  
        print('ВЫМРЕТ 100% ЧЕБУРЕКОВ')
    elif t3>30 and t3<50:
        print('Вымрет 90% чебуреков, но точно не ты')
    else:
        print('Будет чебурекам бобо')
ditch(10000000000,200000000)        
    
    