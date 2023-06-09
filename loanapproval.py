# -*- coding: utf-8 -*-
"""loanapproval.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c_umj4-DNumJHqFwhslYEzv1sID4h-N0

# **Import Libraries**
"""

import numpy as np
import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

data=pd.read_csv("/content/LoanApprovalPrediction.csv")

data







data

"""**Data Exploration**"""

data.head()

data.tail()

data.info()

data.describe()

"""**Data preprocessing/Data Cleaning**

1.Check the datatype
2.Check for missing values
3.Check for duplicates
4.Check for outliers
5.Check for Scaling/Normalization or Standardization
"""

data.dtypes

#Encoding
label_encoder=LabelEncoder()
obj=(data.dtypes == 'object')
for col in list(obj[obj].index):
  data[col]=label_encoder.fit_transform(data[col])

data.dtypes

data.isnull().sum()

#Fill my missing values by the mean(average)
for col in data.columns:
  data[col]=data[col].fillna(data[col].mean())

data.isnull().sum()

#Check for duplicates
data.duplicated().sum()

#check the outliers
import matplotlib.pyplot as plt
plt.figure(figsize=(14,6))
data.boxplot()
# Rotating X-axis labels
plt.xticks(rotation = 90)

#Scaling
data.describe()

data

#Check whether all the columns are required 
data

data.drop(['Loan_ID'],axis=1,inplace=True)

data

#dicide the data into features and target
x=data.drop(['Loan_Status'],axis=1)
y=data.Loan_Status

#Split into training testing 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=7)

x_train.shape

x_test.shape

y_train.shape

y_test.shape

#define the model
model=RidgeClassifier()
model

#fit the model to the training data
model.fit(x_train,y_train)

y_model=model.predict(x_test)

y_test

y_model

accuracy_score(y_test,y_model)*100

cm=confusion_matrix(y_test,y_model)
cm

from sklearn.metrics import classification_report
print(classification_report(y_test,y_model))

with open('train_model.pkl',mode='wb') as pkl:
  pickle.dump(model,pkl)