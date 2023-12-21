#histogram
import matplotlib.pyplot as plt
import numpy as np


#data:[concentrated:170,std:10,population:250]
x_p=np.random.normal(170,10,250)

#plot
plt.hist(x_p)
#show
plt.show()