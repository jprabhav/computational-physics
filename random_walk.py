from numpy import empty,arange,zeros
from matplotlib.pyplot import plot,axes
import matplotlib.animation as animation
from random import randrange
import time
start=time.time()

L=100
N=20000
h=1
pos=[0,0]
array=empty((N,2))
array[0,:]=pos
def walk(pos):
    p=randrange(4)
    x=0
    y=0
    if p==0:
        x=h     #right
    elif p==1:
        x=-h    #left
    elif p==2:
        y=h     #up
    elif p==3:
        y=-h    #down
    
    if pos[0]==L:
        x=-h
    if pos[0]==-L:
        x=h
    if pos[1]==L:
        y=-h
    if pos[1]==-L:
        y=h
    return [pos[0]+x,pos[1]+y]
  
for i in range(1,N):
    array[i,:]=walk(array[i-1,:])

plot(array[:,0],array[:,1],'k', lw=1)



# ANIMATION
'''
fig = plt.figure() 
ax = plt.axes(xlim=(-L,L), ylim=(-L, L)) 
x = xp
line, = ax.plot(xp,f(0))
h=1      #timestep

def init():  
    line.set_ydata([nan] * len(x))
    return line,

def animate(i):
    line.set_ydata(f(i*h)) 
    return line,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=1, blit=True)

plt.show()
'''
end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')