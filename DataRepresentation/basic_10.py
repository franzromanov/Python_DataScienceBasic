#scatter_plt:costumize
import matplotlib.pyplot as plt 
import numpy as np 


x_p=np.array([8,9,1,2,7,5,11,12,10,17])
y_p=np.array([1,3,4,5,6,8,9,3,10,13])
colors=np.array([0,1,2,3,4,5,6,7,8,9])
size=np.array([10,2000,20,200,150,15,40,30,500,50])
plt.scatter(x_p,y_p,c=colors,cmap='spring',s=size,alpha=0.5)
plt.colorbar()
plt.show()