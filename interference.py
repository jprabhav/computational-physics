from numpy import zeros,empty
import time
from pylab import imshow,show,gray,colorbar
from math import pi,sqrt,sin

t=time.time()

array=empty([500,500],float)
k=2*pi/5
for i in range(500):
    for j in range(500):
        r1=sqrt((i-250)**2+(j-200)**2)/5
        r2=sqrt((i-250)**2+(j-300)**2)/5
        array[i,j]=sin(k*r1)+sin(k*r2)

imshow(array, cmap='gray')


s=time.time()
print(s-t)