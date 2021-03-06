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

#forest Decision tree model for non linear data
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy') 
classifier.fit(x_train, y_train)


#predict result
#y_pred = classifier.predict(x_test)

def predictor(data):
    y_pred = classifier.predict(data)
    if y_pred == 0:
        return False
    else:
        return True



















