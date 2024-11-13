import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cleaning
df = pd.read_csv('diabetes.csv')

df.info()

df.describle()
 
df.isnull().sum()

# Libraries
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neighbors import KNeighborsClassifier

# Features
X = df.drop(columns=['Outcome'])   
y = df['Outcome'] 

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# KNN
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

# Metrics
cm = confusion_matrix(y_test,y_pred)

print(cm)
print(classification_report(y_test,y_pred))
