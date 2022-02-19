from numpy import empty,array,dot,zeros,copy
from numpy.linalg import norm
from math import sqrt
import matplotlib.pyplot as plt
from random import random
import matplotlib.animation as animation
import time
start=time.time()


T=100
L=200

spin_u=array([1,0])
spin_d=array([0,1])

psi_p=zeros((2*L+1),complex)
psi_s=zeros((2*L+1,2),complex)

a=100
b=0
psi_p[L+a]=1
psi_s[L+a]=(spin_u+1j*spin_d)

pos=empty(2*L+1)
for i in range(2*L+1):
    pos[i]=i-L


C=array([[1,1],
        [1,-1]],complex)/sqrt(2)



psi_p1=copy(psi_p)
psi_p2=zeros((2*L+1),complex)
psi_s1=copy(psi_s)
psi_s2=zeros((2*L+1,2),complex)
    
for t in range(T):
    for i in range(1,2*L):

        if psi_p1[i]==1:
            psi_s1[i]=dot(C,psi_s1[i])          #Coin operator

    for i in range(1,2*L):
            
        if psi_p1[i]==1:
            
            if psi_s1[i][0]!=0:
                psi_s2[i+1][0]+=psi_s1[i][0]
                psi_p2[i+1]=1
        
            if psi_s1[i][1]!=0:
                psi_s2[i-1][1]+=psi_s1[i][1]
                psi_p2[i-1]=1
    
           
    for i in range(1,2*L):
        count=0
        x=random()
        if psi_p1[b-L]==1:
            continue
        
        elif psi_p1[b-L]==0:
            psi_p2[b-L]=0
            psi_s2[b-L]=[0,0]
    for j in psi_s2:
        count+=norm(j)**2
    
    psi_s2/=sqrt(count)
    
                
    psi_p1=psi_p2
    psi_s1=psi_s2
    psi_p2=zeros((2*L+1),complex)
    psi_s2=zeros((2*L+1,2),complex)
    
prob=empty(2*L+1)
for i in range(2*L+1):
    prob[i]=norm(psi_s1[i])**2

    
amp=prob
plt.plot(pos,amp)
#ANIMATION
'''
fig = plt.figure() 
ax = plt.axes(xlim=(-L,L), ylim=(-0.1, 0.5)) 
x = pos
line, = ax.plot(pos,qw(i))


def init():  
    line.set_ydata([] * len(x))
    return line,

def animate(i):
    line.set_ydata(qw(i)) 
    return line,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=1, blit=True)

plt.show()
'''
end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')
