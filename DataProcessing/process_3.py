import matplotlib.pyplot as plt 
import numpy as np 
from scipy import stats


#data:uniform
data_uni=np.random.uniform(0.0, 5.0, 10000)
data_uniy=np.random.uniform(0.0, 5.0, 10000)
print(f"data={data_uni}")
plt.hist(data_uni)
plt.show()

#data:normal(converge,std,size)
data_norm=np.random.normal(5.0,1.0,10000)
data_normy=np.random.normal(5.0,1.0,10000)
print(f"data={data_norm}")
plt.hist(data_norm,100)
plt.show()


#scatter:uni
plt.scatter(data_uni,data_uniy)
plt.show()


#scatter:norm
plt.scatter(data_norm,data_normy)
plt.show()