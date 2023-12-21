#mean,mode,median
import matplotlib.pyplot as plt 
import numpy as np 
from scipy import stats

#data
data=np.random.randint(1000,size=100)

#show
print(f"data : {data}")

#process
mean_=np.mean(data)#mean
median_=np.median(data)#median
mode_=stats.mode(data)#mode

#show
print(f"""

mean={mean_}
median={median_}
mode={mode_}
	""")
