from numpy import log,sqrt,random
from math import pi
import time
start=time.time()


Z=79
e=1.602e-19
E=7.7e6*e
a0=5.292e-11
eps=8.854e-12
sig=a0/100
N=1e6

b_c=Z*e*e/(2*pi*eps*E)

z=random.rand(N)
r=sqrt(-(2*sig*sig)*log(1-z))

count=0
for i in r:
    if i<b_c:
        count+=1

print(count)

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')