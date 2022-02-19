from pylab import plot,show
from numpy import loadtxt
from numpy.fft import rfft,irfft
import time
start=time.time()

p=loadtxt('dow2.txt')


def smooth(y,r):
    f=rfft(y)
    N=len(f)
    c=int(N*r/100)
    for i in range(c,N):
        f[i]=0
    return irfft(f)

plot(p, 'k')
plot((smooth(p,5)),'r',linewidth=0.9)
show()

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')