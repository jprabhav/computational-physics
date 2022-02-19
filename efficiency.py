from math import exp,sqrt,pi
from gausswx import gaussxw
from pylab import plot,show
from numpy import array,arange,vectorize,loadtxt
import time
start=time.time()


N=100
x,w=gaussxw(N)

#constants
h=6.62e-34
c=3e8
lambda1=390e-9
lambda2=780e-9
kb=1.38e-23
K=h*c/kb


def f(x):
    return (x**3)/(exp(x)-1)

def eta(T):
    
    a=K/(T*lambda2)
    b=K/(T*lambda1) 
    xp=((b-a)*x+(a+b))/2
    wp=(b-a)*w/2
    s=0
    for k in range(N):
        s+=wp[k]*f(xp[k])
    return -s
g=vectorize(eta)
xv=arange(300,10000,1)
plot(xv,g(xv))
show()

z=(1+sqrt(5))/2
epsilon=1e-6

x1=6000
x4=8000
x3=x4/z+(2-z)*x1
x2=x1+x4-x3

while abs(x4-x1)>epsilon:
    if eta(x2)<eta(x3):
        x4=x3
        x3=x4/z+(2-z)*x1
        x2=x1+x4-x3
    else:
        x1=x2
        x3=x4/z+(2-z)*x1
        x2=x1+x4-x3
   
        
p=(x1+x4)/2

print(p,15*eta(p)/(pi**4))

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')