#standard_deviation
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats


#data
data=np.random.randint(100,size=1000)

std_=np.std(data)#std
var_=np.var(data)#variance

#show_data
print(f"data:{data}\n")


print(f"""

	standard_deviation={std_}

	variance={var_}

	""")


#percentile
percentile_=np.percentile(data,75)#75% or lower

print(f"percentile = {percentile_}")