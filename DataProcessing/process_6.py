# Importing the necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer 
from sklearn.compose import ColumnTransformer as ct
from sklearn.preprocessing import OneHotEncoder as ohe, LabelEncoder as le

# Load the dataset
data = pd.read_csv('titanic.csv')
#filter_categoricalTypes
categorical_data=['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']

#show_categorical-data
print(categorical_data)

#transform_categorical
ct_=ct(transformers=[('encoder',ohe(),categorical_data)],remainder='passthrough')
categorical_data=np.array(ct_.fit_transform(data))
print(categorical_data)

#transform_cat_dependant
cat_Dep=data['Survived']
#create_class
le_=le()
cat_Dep=le_.fit_transform(cat_Dep)
print(cat_Dep)

