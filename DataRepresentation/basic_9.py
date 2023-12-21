#scatter_plt:costumize
import matplotlib.pyplot as plt 
import numpy as np 


x_p=np.array([8,9,1,2,7,5])
y_p=np.array([1,3,4,5,6,8])
colors=np.array(['red','blue','yellow','black','magenta','green'])
plt.scatter(x_p,y_p,c=colors)

plt.show()