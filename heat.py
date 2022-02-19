from numpy import empty,copy
from pylab import plot,show
import time
start=time.time()

L=0.01
D=4.25e-6
N=100
a=L/N
h=1e-4

T_low=0
T_mid=20
T_high=50

T=empty(N+1)
T[0]=T_high
T[N]=T_low
T[1:N]=T_mid
Tp=copy(T)

t=0
t1=0.01
t2=0.1
t3=0.4
t4=1
t5=10
epsilon=h/1000
t_end=t5+epsilon

c=(h*D)/(a*a)

while t<t_end:
    
    Tp[1:N]=T[1:N]+c*(T[0:N-1]+T[2:N+1]-2*T[1:N])
    T, Tp = Tp, T
    t+=h
    
    if abs(t-t1)<epsilon:
        plot(T)
    if abs(t-t2)<epsilon:
        plot(T)
    if abs(t-t3)<epsilon:
        plot(T)
    if abs(t-t4)<epsilon:
        plot(T)
    if abs(t-t5)<epsilon:
        plot(T)

show()

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')