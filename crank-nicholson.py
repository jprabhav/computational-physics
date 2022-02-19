from numpy import empty,zeros,arange
from cmath import exp
from pylab import plot,show
from banded import trid
import time
start=time.time()

L=1e-8
M=9.109e-31
x0=L/2
k=5e10
hc=1.054e-34
sig=1e-10+0j
N=1000
a=L/N

h=1e-6       #timestep
t=0
t1=7e-6
epsilon=h/1000

A=zeros((N,N),complex)
B=zeros((N,N),complex)
c=(h*1j*hc)/(4*M*a*a)
a1=1+2*c
a2=-c
b1=1-2*c
b2=c

psi=empty(N,complex)
xp=arange(0,L,a,complex)
def f(x):
    return exp((-(x-x0)**2/(2*sig*sig)))*exp(-1j*k*x)

for i in range(N):
    psi[i]=f(xp[i])


A[0,0]=a1

for i in range(1,N):
    A[i,i-1]=A[i-1,i]=a2
    A[i,i]=a1


while True:
    
    v=zeros(N,complex)
    for i in range(1,N-1):
        v[i]=b1*psi[i]+b2*(psi[i+1]+psi[i-1])

    psi=trid(A,v)
    t+=h
    if abs(t-t1)<epsilon:
        break

plot(psi.real)




end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')