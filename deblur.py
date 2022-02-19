from math import exp
from numpy import loadtxt,empty,arange,flipud,fliplr,zeros,array
from numpy.fft import rfft2,irfft2
from matplotlib.pyplot import imshow, show, subplots
from cv2 import imread
import time
start=time.time()

#image=array(imread('IMG.png', flags=0),float)
image=loadtxt('blur.txt')
k=23

def blur_f(x,y,t):
    return exp(-(x*x+y*y)/(2*t*t))

s=image.shape
a=int(s[0]/2)
b=int(s[1]/2)    
array=empty(s)

for i in range(2*a):
    for j in range(2*b):
        array[i,j]=blur_f(i,j,k)

array[a:,0:b]=flipud(array)[a:,0:b]
array[:,b:]=fliplr(array)[:,b:]
     
b_i=rfft2(image)
f_i=rfft2(array)
final_i=zeros((2*a,b),complex)


epsilon=1e-3
for m in range(2*a):
    for n in range(b):
        if f_i[m,n]>epsilon:
            final_i[m,n]=b_i[m,n]/f_i[m,n]


final=irfft2(final_i)

f, (ax1,ax2)=subplots(1,2, sharey=True)   
ax1.imshow(image,cmap='gray')
ax2.imshow(final,cmap='gray')
show()


end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')
