import matplotlib.pyplot as plt 
import numpy as np 

#declare_points
x_p=np.array([1,8,2])
y_p=np.array([4,6,9])


#labels&title
plt.title("GRAPHICS")
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")

#activate_grid
plt.grid()

#create_plot
plt.plot(x_p,y_p, 'o-r')

#show_plot
plt.show()