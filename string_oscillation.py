from numpy import empty,array,zeros,arange
from pylab import plot,show
from vpython import sphere,rate,vector
from math import cos
import time
start = time.time()

N=20
m=1
c=1
k=6
omega=1
a=2*k-m*omega*omega

A=zeros((N,N))

for i in range(N-1):
    A[i,i+1]=A[i+1,i]=-k
    A[i,i]=a
    
A[0,0]=A[N-1,N-1]=a-k

v=zeros(N)
v[0]=c

for i in range(N-1):
        
    q=A[i,i]
    A[i,:]=A[i,:]/q
    v[i]=v[i]/q
    v[i+1]-=A[i+1,i]*v[i]
    A[i+1,:]-=A[i+1,i]*A[i,:]

v[N-1]/=A[N-1,N-1] 
A[N-1,:]/=A[N-1,N-1]


x=empty(N)

x[N-1]=v[N-1]
for i in range(N-2,-1,-1):
    x[i]=v[i]-A[i,i+1]*x[i+1]
    
#Visualization

'''
s = empty(N,sphere)
for t in arange(0,100,0.1):
    rate(30)
    for i in range(N):
        s[i]=sphere(pos=vector(0+2*i,x[1]*cos(omega*t),0),radius=0.2)

'''



plot(x)
plot(x,'ko')
show()
      
end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')
