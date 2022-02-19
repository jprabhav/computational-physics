from numpy import empty, array, eye, dot, copy
import time
start = time.time()

M=array([[3,0,2],
         [2,0,-2],
         [0,1,1]],float)

N=len(M)

def solve(T,b):

    A=copy(T)
    v=copy(b)
    for m in range(N):
        #Pivoting, you can ignore it for now.
        for i in range(m+1,N):
            if A[m,m] < A[i,m]:
                A[[m,i],:]=A[[i,m],:]	
                v[[m,i]]=v[[i,m]]
	
        # Divide by the diagonal element
        div=A[m,m]
        A[m,:]/=div
        v[m]/=div

        # Now subtract from the lower rows
        for i in range(m+1,N):
            mult=A[i,m]
            A[i,:]-=mult*A[m,:]
            v[i]-=mult*v[m]

    # Backsubstitution
    x=empty(N,float)
    for m in range(N-1,-1,-1):
        x[m]=v[m]
        for i in range(m+1,N):
            x[m]-=A[m,i]*x[i]

    return x


# Simply calculate the inverse by solving the system of equations where the
# columns are from the Identity matrix.
def inverse(A): 
    T=copy(A)
    B=empty((N,N),float)
    I=eye(N)
    for i in range(N):
        B[:,i]=solve(T,I[:,i])
    return B

S=inverse(M)
T=dot(M,S)



end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')
