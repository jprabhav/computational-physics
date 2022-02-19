from numpy import empty,copy
from pylab import plot,show
from math import sin,pi
import time
start=time.time()

L=20
D=0.1
N=100
a=L/N
h=0.2


def temp(t):
    return 10 + 12*sin(2*pi*t/365)

T_up=10
T_mid=10
T_down=11

T=empty(N+1)
T[0]=T_up
T[N]=T_down
T[1:N]=T_mid
Tp=copy(T)

t=0
t5=3650
epsilon=h/1000
t_end=t5+epsilon

c=(h*D)/(a*a)

while t<t_end:
    
    T[0]=temp(t)
    Tp[1:N]=T[1:N]+c*(T[0:N-1]+T[2:N+1]-2*T[1:N])
    T, Tp = Tp, T
    t+=h
    
    if abs(t-(t5-(90*1)))<epsilon:
        plot(T,'r')
    if abs(t-(t5-(90*3)))<epsilon:
        plot(T ,'g')
    if abs(t-(t5-(90*2)))<epsilon:
        plot(T,'b')
    if abs(t-(t5-(90*4)))<epsilon:
        plot(T, 'k')
show()

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')