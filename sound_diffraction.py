from gausswx import gaussxw
from math import exp,sqrt,cos,pi,sin
from pylab import plot,show, imshow
from numpy import arange,vectorize,empty
import time
start = time.time()

N=20
x,w=gaussxw(N)


def I(y,z):
    u=y*sqrt(2/z)
    
    def f(t):
        return cos(pi*(t**2)/2)
    def g(t):
        return sin(pi*(t**2)/2)
    
    a=0
    b=u
    xp=((b-a)*x+(b+a))/2
    wp=(b-a)*w/2
    
    s=0
    t=0
    for k in range(N):
        s+=wp[k]*f(xp[k])
        t+=wp[k]*g(xp[k])
    
    return ((2*s+1)**2+(2*t+1)**2)/8

n=100
arr=empty((n,n))

for i in range(n):
    for j in range(n):
        if j<=n/2:
            arr[i,j]=1
            
        elif i==j==n/2:
            arr[i,j]=0
            
        else:
            x1=(i-n/2)
            y1=(j-n/2)
            arr[i,j]=I(x1,abs(y1))
    
imshow(arr, vmax=0.5)

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')
