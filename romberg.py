from math import exp,sin,cos,pi,sqrt
import time
start = time.time()


def f(x):
    return (sin(sqrt(100*x)))**2

a=0
b=1


def s_i(i):
    
        s=f(a)+f(b)
        h=(b-a)/n
        for i in range(1,n,2):
            s+=4*f(a+i*h)
    
        for j in range(2,n,2):
            s+=2*f(a+j*h)
        return s*h/3


n_0=10
s=(f(a)+f(b))/3
h0=(b-a)/n_0
for i in range(2,n_0,2):
    s+=(2/3)*f(a+i*h0)
    
I=10

def ti(i):
    t=0
    n=(2**i)*(n_0)
    hi=(b-a)/n
    t=0
    for j in range(1,n,2):
        t+=2*f(a+j*hi)/3
    return t


for i in range(1,I):
    n=(2**i)*(n_0)
    hi=(b-a)/n
    
    t=ti(i)   
    p_i=hi*(s+2*t)
    s=s+t

print(p_i)
    

    


    
    



end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')


            

            
            