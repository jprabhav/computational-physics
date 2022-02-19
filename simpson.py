import time
start = time.time()


def f(x):
    return x

a=0
b=1

def trap(a,b,n):
    s=(f(a)+f(b))/2
    h=(b-a)/n
    for i in range(1,n):
           s+=f(a+i*h)
    return s*h
    
def simp(a,b,n):
    
        s=f(a)+f(b)
        h=(b-a)/n
        for i in range(1,n,2):
            s+=4*f(a+i*h)
    
        for j in range(2,n,2):
            s+=2*f(a+j*h)
        return s*h/3


    
end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')


            

            
            