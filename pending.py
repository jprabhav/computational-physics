from gausswx import gaussxw
from pylab import imshow
from numpy import empty
from math import sqrt,atan,pi,sin
import time
start = time.time()




N=15
x,w=gaussxw(N)

a=0.1
x1=-a
x2=a
y1=-a
y2=a
xp=((x2-x1)*x+(x2+x1))/2
yp=((y2-y1)*x+(y2+y1))/2
wx=(x2-x1)*w/2
wy=(y2-y1)*w/2

 
def f(x,y):
        return 1/sqrt(x*x+y*y)
    
def d(x,y):
    return sin(2*pi*x/a)*sin(2*pi*y/a)

def V(y,z):
    
    s=0
    for i in range(N):
        for k in range(N):
            s+=wx[i]*wy[k]*d(xp[i],yp[k])*f(xp[i]-y,yp[k]-z)
    return s


def pfx(x,y):
    h=1e-6
    return (f(x+h/2,y)-f(x-h/2,y))/h

def pfy(x,y):
    h=1e-6
    return (f(x,y+h/2)-f(x,y-h/2))/h

def E(x,y):
    if pfx(x,y)==0 and pfy(x,y)>0:
        return pi/2
    elif pfx(x,y)==0 and pfy(x,y)<=0:
        return pi/2
    else:
        return atan(pfy(x,y)/pfx(x,y))

print(pfx(0.1,0))




d=1
n=100
arr=empty((n,n))
for i in range(n):
    for j in range(n):
        r1,r2=n/2,n/2
        q=(i-n/2)*d/n
        p=(j-n/2)*d/n
        arr[i,j]=V(p,q)

imshow(arr)



end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')
