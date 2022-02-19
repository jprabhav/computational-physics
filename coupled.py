from math import sin
from numpy import empty,arange,array
from pylab import plot
import time
start=time.time()


sig=10
p=28
q=8/3

def f(r,t):
    x=r[0]
    y=r[1]
    z=r[2]
    fx=sig*(y-x)                            #diffeq here
    fy=x*(p-z)-y
    fz=x*y-q*z
    return array([fx,fy,fz],float)

a=0
b=30
N=3000
h=(b-a)/N

r=empty((N,3))
tp=arange(a,b,h)    
r[0]=[0,1,0]

for i in range(1,N):
    r[i]=r[i-1]+h*(f(r[i-1],tp[i]))

plot(r[:,0],r[:,2])


end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')