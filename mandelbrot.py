from numpy import empty
from pylab import imshow,show
from math import log
import time
t=time.time()

n=400
it=400
array=empty([n,n])
xrange=2
scale=1.5      #default 2 , works inversly
epsilon=1
for i in range(int(n/2)):
    for k in range(n):
        z=0
        c=scale*xrange*complex((k-(n/1.4)),(i-(n/2)))/n
        counter=0
        for m in range(it):
            z=z*z+c
            if abs(z)>2:
                counter=m
                break
            else:
                counter=it
        array[i,k]=counter
        array[n-1-i,k]=counter
        #array[i,k]=log(counter+epsilon)              #uncomment for logarithm plot
        #array[n-1-i,k]=log(counter+epsilon)
        

imshow(array, cmap='jet')
show()
            

s=time.time()
print(s-t)