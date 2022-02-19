from gausswx import gaussxw
from pylab import imshow
from numpy import empty
import time
start = time.time()


N=15
x,w=gaussxw(N)

a=2
b=3
x1=-a
x2=a
y1=-b
y2=b
xp=((x2-x1)*x+(x2+x1))/2
yp=((y2-y1)*x+(y2+y1))/2
wx=(x2-x1)*w/2
wy=(y2-y1)*w/2
 
def f(x,y,z):
        return 1/(x*x+y*y+z*z)**1.5

def g(a,b,z):
   
    s=0
    for i in range(N):
        for k in range(N):
            s+=wx[i]*wy[k]*f(xp[i]-a,yp[k]-b,z)
    return s

d=15
h=1
n=100
arr=empty((n,n))
for i in range(n):
    for j in range(n):
        r1,r2=n/2,n/2
        p=(i-r1)*d/n
        q=(j-r2)*d/n
        arr[i,j]=g(p,q,h)

imshow(arr)



end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')
