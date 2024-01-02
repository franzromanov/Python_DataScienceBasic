# Import necessary libraries
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
# Load the Iris dataset
data=pd.read_csv('iris.csv')

# Separate features and target
X=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

# Split the dataset into an 80-20 training-test set
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
scaler=StandardScaler()
# Apply feature scaling on the training and test sets

X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
#y_train=scaler.fit_transform(y_train)
#y_test=scaler.fit_transform(y_test)


print(X_train)
print(X_test)
print(y_test)
print(X_train)

# Print the scaled training and test sets