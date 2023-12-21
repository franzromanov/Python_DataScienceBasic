import matplotlib.pyplot as plt 
import numpy as np 

#declare_points
x_p=np.array([1,2,3])
y_p=np.array([5,6,7])

plt.subplot(1,2,1)
plt.title("copper")
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.grid()
plt.plot(x_p,y_p,'o:b')

#declare_points
x_p=np.array([1,2,3])
y_p=np.array([7,11,21])

plt.subplot(1,2,2)
plt.title("silver")
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.grid()
plt.plot(x_p,y_p,'o-r')

plt.suptitle("RESISTANCE")

plt.show()