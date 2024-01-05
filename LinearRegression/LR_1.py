import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

#csv
data=pd.read_csv('Salary_Data.csv')
X=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

#split
X_train,X_test, y_train, y_test= train_test_split(X,y,test_size=0.2,random_state=100)

#training
regression_=LinearRegression()
regression_.fit(X_train,y_train)

#predict
predict_y=regression_.predict(X_test)

#display_training
plt.subplot(1,2,1)
plt.title('Training Set')
plt.xlabel('Years')
plt.ylabel('Salary')
plt.grid()
plt.scatter(X_train,y_train,color='black')
plt.plot(X_train,regression_.predict(X_train))

#display_test

plt.subplot(1,2,2)
plt.title('Test Set')
plt.xlabel('Years')
plt.ylabel('Salary')
plt.grid()
plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,regression_.predict(X_train))
plt.suptitle('Salary Vs Years Of Experience')
plt.show()