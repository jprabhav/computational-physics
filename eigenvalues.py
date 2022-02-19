from numpy import sqrt,empty,array,zeros,eye
import time
start = time.time()


def norm(x):
    return sqrt(x.dot(x))

#input values
n=4
A=array([[1,4,8,4],
         [4,2,3,7],
         [8,3,6,9],
         [4,7,9,2]]) 
    
#calculates QR decomposition
def QR(A):
    U=empty((n,n))
    Q=empty((n,n))
    R=zeros((n,n))

    U[:,0]=A[:,0]
    Q[:,0]=U[:,0]/norm(U[:,0])

    for i in range(1,n):
        s=zeros(n)
        for j in range(0,i):
            s-=(Q[:,j].dot(A[:,i]))*Q[:,j]
        U[:,i]=A[:,i]+s
        Q[:,i]=U[:,i]/norm(U[:,i])

    for i in range(n):
        R[i,i]=norm(U[:,i])
        for j in range(i+1,n):
            R[i,j]=Q[:,i].dot(A[:,j])
    return Q , R    


def eigen(A):
    epsilon=1e-13
    V=eye(n)
    eigen=empty(n)

    while True:
        Q,R=QR(A)
        A=R.dot(Q)
        V=V.dot(Q)
        counter=True
        for i in range(n):
            eigen[i]=A[i,i]
            for j in range(n):
                if  i !=j and abs(A[i,j])>epsilon:
                    counter=counter and False
        if counter == True:
            break
    return V,eigen


print(eigen(A))


end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')