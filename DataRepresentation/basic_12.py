#bars
import matplotlib.pyplot as plt 
import numpy as np 

#data
x_p=np.array(['A','B','C','D'])
y_p=np.array([3,4,1,5])

#plot
plt.bar(x_p,y_p)
plt.title("RESULT")
plt.xlabel('domain')
plt.ylabel('range')

#show
plt.show()
