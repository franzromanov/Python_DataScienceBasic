import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.impute import SimpleImputer as si 
import pandas as pd
from sklearn.compose import ColumnTransformer as ct 
from sklearn.preprocessing import OneHotEncoder as ohe 
from sklearn.preprocessing import LabelEncoder as le 
import math

#read_csv
data=pd.read_csv('Data.csv')

#data
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

#missing_val
filter_=[]

for rows in x:
	for cols in rows:
		try:
			if math.isnan(float(cols))==1:
				filter_.append(list(rows))
		except:
			continue

#casting
filter_=np.array(filter_)
print(filter_)

#imputing
impute_=si(missing_values=np.nan,strategy='mean')
impute_.fit(x[:,1:3])
x[:,1:3]=impute_.transform(x[:,1:3])
print(x)

#encoding_independent_CatVal
ct_=ct(transformers=[('encoder',ohe(),[0])],remainder='passthrough')
x=np.array(ct_.fit_transform(x))
print(x)

#encoding_dependent_CatVal
le_=le()
y=le_.fit_transform(y)
print(y)






