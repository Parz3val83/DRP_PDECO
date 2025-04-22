import numpy as np
import matplotlib.pyplot as plt


def y(x_val):
    return np.sin(2*np.pi*x_val)

def u(x_val):
    
    return 2*x_val

n_1=13
x_step=np.arange(0,1+1/n_1,1/n_1 )



print(x_step)









plt.plot(x_step,y(x_step))
plt.plot(x_step,u(x_step))

plt.show
