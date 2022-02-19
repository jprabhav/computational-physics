from numpy import empty,arange
from cmath import exp
from math import pi,cos,sin
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from dcst import dst,idst
import time
start=time.time()

L=1e-8
M=9.109e-31
x0=L/2
k=5e10
hc=1.054e-34
sig=1e-10
N=1000
a=L/N
c=(pi*pi*hc)/(2*M*L*L)


psi=empty(N,complex)
xp=arange(0,L,a)

def f(x):
    return exp((-(x-x0)**2/(2*sig*sig)))*exp(-1j*k*x)

for i in range(N):
    psi[i]=f(xp[i])


ak=dst(psi.real)
ck=dst(psi.imag)

def f(t):
    p=empty(ak.shape)
    for i in range(1,N):
        p[i]=ak[i]*cos(c*i*i*t)-ck[i]*sin(c*i*i*t)
    return idst(p)


#ANIMATION PART

fig = plt.figure() 
ax = plt.axes(xlim=(0,L), ylim=(-1, 1)) 
x = xp
line, = ax.plot(xp,f(0))
h=1e-18      #timestep

def init():  
    line.set_ydata([] * len(x))
    return line,

def animate(i):
    line.set_ydata(f(i*h)) 
    return line,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=1, blit=True)

#ani.save("movie.mp4")
plt.show()
end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')