#classification

import numpy as np
import pandas as pd

dataset = pd.read_csv('mamba_data2.csv')
x = dataset.iloc[:,1:18]
y = dataset.iloc[:,18]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=0)

#feature scaling required to predict accurate results
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test) 



# 1) KNN k-nearest neighbour model for non linear
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p=2)
classifier.fit(x_train, y_train)



# 2) kernel SVM support vector machine model for non linear data
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state=0) 
classifier.fit(x_train, y_train)

# 3) naive Bayes  model for non linear data
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB() 
classifier.fit(x_train, y_train)

# 4) Decision tree model for non linear data
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0) 
classifier.fit(x_train, y_train)

# 5) Random forest model for non linear data
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy') 
classifier.fit(x_train, y_train)

#predict result
y_pred = classifier.predict(x_test)

#evaluate performance using cnfusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)

























