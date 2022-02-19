from math import exp,sqrt
import time
start=time.time()


def f(x):
    return x**(-6)-exp(-x)

z=(1+sqrt(5))/2


epsilon=1e-6

x1=0
x4=3
x3=x4/z+(2-z)*x1
x2=x1+x4-x3

while abs(x4-x1)>epsilon:
    if f(x2)<f(x3):
        x4=x3
        x3=x4/z+(2-z)*x1
        x2=x1+x4-x3
    else:
        x1=x2
        x3=x4/z+(2-z)*x1
        x2=x1+x4-x3
   
        
x=(x1+x4)/2

print(x,f(x))

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')