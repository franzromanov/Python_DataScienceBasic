#scatter_plot
import matplotlib.pyplot as plt 
import numpy as np 

#first_data
x_p=([1,2,3,4])
y_p=([5,6,2,1])

plt.scatter(x_p,y_p)#plot

#second_data
x_p=([3,4,5,6])
y_p=([1,2,9,8])

plt.scatter(x_p,y_p)#plot

#show_plot
plt.title("Age Vs Sales")
plt.xlabel("Age")
plt.ylabel("Sales")
plt.grid()
plt.show()