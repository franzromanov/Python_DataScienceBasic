#bar
import numpy as np 
import matplotlib.pyplot as plt 

#data
x_p=np.array(['A','B','C','D','E'])
y_p=np.random.randint(50,size=5);


#plot
plt.title('Function')
plt.xlabel('Domain')
plt.ylabel('Range')
plt.barh(x_p,y_p,color='magenta', height=0.35)

#show
plt.show()