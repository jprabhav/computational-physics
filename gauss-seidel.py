from numpy import empty,zeros,max,copy
from pylab import imshow
import time
start=time.time()


V=1
a=1
M=100
epsilon=1e-6

omega=0.94 #overrelaxation parameter

phi=zeros((M+1,M+1))
phi[20:80,20]=V
phi[20:80,80]=-V

delta=1
while delta>epsilon:
    y=copy(phi)
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or j==0 or j==M or i==M:        #outer boundary
                continue
            elif (j==20 and i<=80 and i>=20) or (j==80 and i<=80 and i>=20):
                continue
            else:
                #phi[i,j]=(phi[i+a,j]+phi[i,j+a]+phi[i-a,j]+phi[i,j-a])/4  #Gauss-Seidel
                phi[i,j]=((phi[i+a,j]+phi[i,j+a]+phi[i-a,j]+phi[i,j-a])*(1+omega))/4 -(omega*phi[i,j])
    delta=max(abs(y-phi))
    
imshow(phi)
    

end = time.time()
print('The code executed in', "%.4f" % (end - start)+'s.')