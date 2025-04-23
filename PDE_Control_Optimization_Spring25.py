#Libraries
import numpy as np
import matplotlib.pyplot as plt

def D_Lap(N):
    h = 1/(N-1)
    A = np.diag([-2.0]*N)
    A += np.diag([1.0]*(N-1),1)
    A += np.diag([1.0]*(N-1),-1)
    A[0,1] = A[N-1,N-2] = 0
    A[0,0] = A[N-1,N-1] = h**2
    return A/h**2

#Setup
N = 100
x = np.linspace(0,1,N)
y_omega = np.sin(2*np.pi*x)
u = -1*np.sin(np.pi*x)
Beta = 1
alpha = 1
D = D_Lap(N)
tol = 10**-4

y1 = 0*x
y2 = 0*x
y3 = 0*x
u1 = 0*x
u2 = 0*x
u3 = 0*x

#Iterate until beats error tolerance
y = 0.0*x #Ghost fnc
sup_E = np.max(np.abs(y-y_omega))
i=0
while sup_E>tol:
    y = np.linalg.solve(-1*D,Beta*u)
    y[0] = y[N-1] = 0
    p = np.linalg.solve(-1*D,y-y_omega)
    p[0] = p[N-1] = 0
    u_old = u
    u = u - alpha*(Beta*p)
    if i == 0:
        y1 = y
        u1 = u
    if i == 3000:
        y2 = y
        u2 = u
    if i == 6000:
        y3 = y
        u3 = u
    sup_E = np.max(np.abs(u-u_old))
    i += 1

print(i)
fig, axes = plt.subplots(nrows=2, ncols=4)
axes[0,0].plot(x,y1)
axes[0,0].plot(x,y_omega)
axes[0,1].plot(x,u1)
axes[0,0].set_title('Snapshot 1')
axes[0,1].set_title('Control Snapshot 1')
axes[0,2].plot(x,y2)
axes[0,2].plot(x,y_omega)
axes[0,3].plot(x,u2)
axes[0,2].set_title('Snapshot 2')
axes[0,3].set_title('Control Snapshot 2')
axes[1,0].plot(x,y3)
axes[1,0].plot(x,y_omega)
axes[1,1].plot(x,u3)
axes[1,0].set_title('Snapshot 3')
axes[1,1].set_title('Control Snapshot 3')
axes[1,2].plot(x,y)
axes[1,2].plot(x,y_omega)
axes[1,3].plot(x,u)
axes[1,2].set_title('Final')
axes[1,3].set_title('Control Final')
plt.tight_layout()

plt.show()