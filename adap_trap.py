from math import exp,sin,cos,pi,sqrt
import time
start = time.time()


def f(x):
    return (sin(sqrt(100*x)))**2

a=0
b=1

def trap(a,b,n):
    s=(f(a)+f(b))/2
    h=(b-a)/n
    for i in range(1,n):
           s+=f(a+i*h)
    return s*h
    
def simp(a,b,n):
    
        s=f(a)+f(b)
        h=(b-a)/n
        for i in range(1,n,2):
            s+=4*f(a+i*h)
    
        for j in range(2,n,2):
            s+=2*f(a+j*h)
        return s*h/3


n_0=10
q=trap(a,b,n_0)
I=20
def R_i1(I):
    q=trap(a,b,n_0)
    for i in range(1,I):
        n=(2**i)*(n_0)
        hi=(b-a)/n
        s=0
        for j in range(1,n,2):
            s+=hi*f(a+j*hi)
        p_i=q/2+s
        q=p_i
       #err=(p_i-q)/2
    return p_i
    
def R(i,m):
    if m>i:
        return 'Fuck off!'
    if i==1:
        return q
    if m==1:
        return R_i1(i)
    err=(R(i,m-1)-R(i-1,m-1))/(4**(m-1)-1)
    return R(i,m-1)+err

def err(i):
    return (R(i,i-1)-R(i-1,i-1))/(4**(i-1)-1)

err(2)
print(err(5))
print(R(5,5))

    
    



end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')


            

            
            