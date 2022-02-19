from numpy import empty,zeros,copy,array,identity,dot
from numpy.linalg import norm
#from pylab import imshow
from math import sqrt
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import time
start=time.time()

N=1
J=5
h=3

t=10
dt=0.1
step=int(t/dt)

sig_z=array(([1,0],[0,-1]),complex)
I=identity(2,complex)
H=h*sig_z
U=I-(dt*1j)*H-(dt**2)*dot(H,H)

psi=zeros((2,N),complex)
psi[0]=1/sqrt(2)
psi[1]=-1/sqrt(2)

def evol(psi,n):
    psi_1=copy(psi)
    for i in range(n):
        psi_1=dot(U,psi_1)
    
    return psi_1


def prob(psi): 
    
    p=empty(N)
    for i in range(N):
        p[i]=norm(psi[i])**2
    
    return p

a=evol(psi,1)

'''
b=empty(step)
for i in range(step):
    b[i]=prob(evol(psi,i))
    
#ANIMATION

fig = plt.figure() 
ax = plt.axes(xlim=(-L,L), ylim=(-0.1, 0.2)) 
x = pos
line, = ax.plot(pos,prob(a[1]))

def init():  
    line.set_ydata([]*len(x))
    return line,

def animate(i):
    
    
    return line,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=0.5, blit=True)

plt.show()
'''



end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')