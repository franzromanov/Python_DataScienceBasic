import matplotlib.pyplot as plt 
import numpy as np 

#points
x_p= np.random.randint(500,size=(100))
y_p= np.random.randint(200,size=(100))

#properties
colors=np.random.randint(100,size=(100))
size=10*np.random.randint(100,size=(100))

#plot
plt.scatter(x_p,y_p, c=colors,s=size,alpha=0.5, cmap='magma')
plt.colorbar()
plt.show()