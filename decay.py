from pylab import plot
from random import random
from numpy import arange
import time
start=time.time()

Bi=1000
Tl=0
Pb=0
Bis=0
tau1=46*60
tau2=2.2*60
tau3=3.3*60

h=1
t=2000

p1=1-2**(-h/tau1)
p2=1-2**(-h/tau2)
p3=1-2**(-h/tau3)



tp=arange(0,t,h)

Bip=[]
Tlp=[]
Pbp=[]
Bisp=[]
for t in tp:
    Tlp.append(Tl)
    Pbp.append(Pb)
    Bip.append(Bi)
    Bisp.append(Bis)
    
    d1=0
    d2=0
    d3=0
    d4=0
    for i in range(Pb):
        if random()<p3:
            d1+=1
    for i in range(Tl):
        if random()<p2:
            d2+=1
    for i in range(Bi):
        if random()<p3:
            if random()<0.97:
                d3+=1
            else:
                d4+=1
    
    Pb-=d1
    Bis+=d1
    Tl-=d2
    Pb+=d2
    Bi-=d3+d4
    Tl+=d4
    Pb+=d3
    
plot(tp,Tlp,'r')
plot(tp,Pbp,'b')
plot(tp,Bip,'g')
plot(tp,Bisp,'k')    

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')