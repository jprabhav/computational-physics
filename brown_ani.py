from numpy import empty
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from random import randrange
import time
start=time.time()

L=100
N=20000
h=1
pos=[0,0,0]
array=empty((N,3))
array[0,:]=pos

def walk(pos):
    p=randrange(6)
    x=0
    y=0
    z=0
    if p==0:
        x=h     #right
    elif p==1:
        x=-h    #left
    elif p==2:
        y=h     #up
    elif p==3:
        y=-h    #down
    elif p==4:
        z=-h    #down
    elif p==5:
        z=h    #down
    
    if pos[0]==L:
        x=-h
    if pos[0]==-L:
        x=h
    if pos[1]==L:
        y=-h
    if pos[1]==-L:
        y=h
    if pos[2]==-L:
        z=h
    if pos[2]==-L:
        z=h
    return [pos[0]+x,pos[1]+y,pos[2]+z]
  
for i in range(1,N):
    array[i,:]=walk(array[i-1,:])

'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(array[:,0], array[:,1], array[:,2], 'k', lw=0.8)
'''
a=array
b=array
#ANIMATION

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = pos
g, = ax.plot(pos,pos,pos)

def init():  
    g.set_data()
    return g,

def animate(i):
    global b
    global a
    b[i,:]=walk(a[i-1,:])
    g.set_data(b[:,0], b[:,1], b[:,2])
    a=b
    return g,

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=1, blit=True)

plt.show()

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')