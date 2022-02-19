from math import sin
from random import random
import time
start=time.time()


def f(x):
    return sin(1/(x*(2-x)))**2

a=0
b=2
h=1
N=10000

def monte_c(N):
    S=0
    for i in range(N):
        x,y=a+random()*(b-a),random()*h
        if y<f(x):
            S+=1
    return S*(b-a)/N

def mean_v(N):
    S=0
    for i in range(N):
        x=a+random()*(b-a)
        S+=f(x)
    return (b-a)*S/N


print(monte_c(N))
print(mean_v(N))


end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')