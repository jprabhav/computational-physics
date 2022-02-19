from math import pi,sin
from numpy import empty,vectorize,linspace
from numpy.linalg import eigh
from pylab import plot,show
import time
start = time.time()



#constants
h=6.62e-34
m_e=9.1e-31
eV=1.6e-19
L=5e-10
a=(10)*eV
k1=(h*h)/(8*m_e*L*L)
k2=-(8*a)/(pi*pi)


n=1000
H=empty((n,n))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            H[i-1,j-1]=(j*j)*k1+(a/2)
        elif i!=j and (i+j)%2==0:
            H[i-1,j-1]=0
        elif i!=j and (i+j)%2==1:
            H[i-1,j-1]=k2*i*j/((i*i-j*j)**2)
            
v=eigh(H)[1]

def psi(m,x):
    v_n=v[:,m-1]
    s=0
    for i in range(n):
        s+=v_n[i]*sin(i*pi*x/L)
    return s

def p1(x):
    return psi(1,x)
def p2(x):
    return psi(2,x)
def p3(x):
    return psi(3,x)

p=vectorize(p1)
q=vectorize(p2)
r=vectorize(p3)

#plotting
xv=linspace(0,L,100)
yv1=p(xv)**2
yv2=q(xv)**2
yv3=r(xv)**2
plot(xv,yv1)
plot(xv,yv2)
plot(xv,yv3)
show()
            
end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')