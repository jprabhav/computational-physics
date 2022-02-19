import numpy as np
from math import exp,sin,cos,pi,sqrt
from pylab import plot,show,imshow
import time
start = time.time()

def  j(m,x):
    def f(phi):
        return cos(m*phi-(x*sin(phi)))
    def simp(a,b,n):
    
        s=f(a)+f(b)
        h=(b-a)/n
        for i in range(1,n,2):
            s+=4*f(a+i*h)
    
        for j in range(2,n,2):
            s+=2*f(a+j*h)
            return s*h/3
    
    return simp(0,pi,10)/pi

def j0(x):
    return j(0,x)

def j1(x):
    return j(1,x)

def j2(x):
    return j(2,x)
    

n=500
iar=np.empty((n,n))
lambd=0.5
k=(2*pi/lambd)
d=2

for i in range(n):
    for l in range(n):
        r=sqrt((i-(n/2))**2+(l-(n/2))**2)*(d/n)
        if r==0:
            iar[i,l]=0.5
        else:
            iar[i,l]=(j1(k*r)/(k*r))**2

imshow(iar, cmap='hot', vmax=0.01)





end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')


            

            
            