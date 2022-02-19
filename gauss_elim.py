from numpy import empty,array
import time
start = time.time()


A=array([[3,0,2],
         [2,0,-2],
         [0,1,1]],float)

v=array([1,0,0],float)
N=len(A)

for i in range(N):
    
    if A[i,i]==0:
        for j in range(i+1,N):
            if A[j,i]!=0:
                A[[i,j]]=A[[j,i]]
    
    q=A[i,i]
    A[i,:]=A[i,:]/q
    v[i]=v[i]/q
    
    for j in range(i+1,N):
        A[j,:]-=A[j,i]*A[i,:]
        v[j]-=A[j,i]*v[i]
       
        


x=empty(N,float)
for i in range(N-1,-1,-1):
    x[i]=v[i]
    for j in range(i+1,N):
        x[i]-=A[i,j]*x[j]
    
print(x)
        


end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')
