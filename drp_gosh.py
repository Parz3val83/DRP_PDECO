import numpy as np
import matplotlib.pyplot as plt

def y(x_val):
    return np.sin(2*np.pi*x_val)

def u_0(x_val):
    
    return np.sin(x_val)



n_1=10
n=n_1+1
h=1/n_1
    
d=np.zeros((n,n))
np.fill_diagonal(d, -2)
np.fill_diagonal(d[1:], 1)
np.fill_diagonal(d[:,1:],1)

d[0,0]= h**2
d[0,1]=0
d[n_1,n_1]=h**2
d[n_1,n_1-1]=0
d=d*1/(h**2)

x_step=np.linspace(0,1,n)

u_n=u_0(x_step)

y_b=np.zeros(n_1)

stp=1

a=1 

while stp > 0.01:
    
    
    y_n=-1*(np.linalg.solve(d, u_n))

    p_n=-1*(np.linalg.solve(d, y_n))
    
    u_n= u_n-(a*(u_n-p_n))
    
    stp= np.linalg.norm(y_n)-np.linalg.norm(u_n)
    
    plt.plot(x_step,u_n)
    
    


print(p_n)
print(y_n)




#plt.plot(x_step,y(x_step))

plt.show
