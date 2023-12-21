#piechart
import matplotlib.pyplot as plt 
import numpy as np 

ratio=np.array([15,25,25,35])
label=np.array(['toyota','honda','bmw','ford'])
expl=np.array([0.5,0.2,0.1,0])
clr=np.array(['magenta','indigo','lime','cyan'])
#plot
plt.pie(ratio,labels=label,startangle=90,explode=expl,shadow=True,colors=clr)
plt.legend(title='car brand:')
#show
plt.show()