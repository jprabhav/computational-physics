from numpy import empty,array
import time
start = time.time()

A=array([[3,0,2],
         [2,0,-2],
         [0,1,1]],float)

v=array([0,1,0],float)
N=len(v)

for m in range(N):
	
    # Check if A[m,m] is the largest value from elements bellow and perform swapping
	
    for i in range(m+1,N):
        if A[m,m] < A[i,m]:
            A[[m,i],:] = A[[i,m],:]	
            v[[m,i]] = v[[i,m]]
	
    # Divide by the diagonal element
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div

    # Now subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

# Backsubstitution
x = empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]


    
print(x)
        


end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')
