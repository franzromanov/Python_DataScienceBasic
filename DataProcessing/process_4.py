import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import math 
from sklearn.impute import SimpleImputer

#read_csv_file
dataset = pd.read_csv('Data.csv')

#get_as_a_matrices
x_p=dataset.iloc[:,:-1].values#all row and all column except last collumn
y_p=dataset.iloc[:,-1].values#all row and last collumn

#filtered_list
filtered=[]

#filtering
for rows in x_p:
	for cols in rows:
		try:
			if math.isnan(float(cols))==1:
				filtered.append(list(rows))
		except:
			continue

#casting
filtered=np.array(filtered)

#before_imputing
print(x_p)
print(y_p)

#show_missing_data
print(filtered)

#missing_data
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x_p[:, 1:3])
x_p[:, 1:3] = imputer.transform(x_p[:, 1:3])
print(x_p)