# -*- coding: utf-8 -*-
"""treinamento.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aIayeiVPJK5tYk5K5l69yN9WF2C5twr3
"""

import numpy as np
import pandas as pd
import sklearn.metrics as m

import os
import tarfile
from six.moves import urllib

FILE_TO_DOWNLOAD =  "Dados.csv"
DATA_PATH = "treinamento/"
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/GabrielVantuil/ect2702-ml/master/classificacao-svm/"
DATA_URL = DOWNLOAD_ROOT + DATA_PATH + FILE_TO_DOWNLOAD
def fetch_data(data_url=DATA_URL, data_path=DATA_PATH, file_to_download=FILE_TO_DOWNLOAD):
  if not os.path.isdir(data_path):
    os.makedirs(data_path)
  urllib.request.urlretrieve(data_url, data_path+file_to_download)  
fetch_data() 

# Importando dados do arquivo
dataset = pd.read_csv(DATA_PATH+FILE_TO_DOWNLOAD)

X = dataset.iloc[:,:3].values
y = dataset.iloc[:,3].values

# Dividindo o banco de dados entre treinamento e teste
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(decision_function_shape='ovo')

classifier.fit(X_train, y_train)

C_2d_range = np.logspace(-2,10,30)

gamma_2d_range = np.logspace(-9,3,30)

classifiers = []

for C in C_2d_range:
    for gamma in gamma_2d_range:
        classifier = SVC(C=C, gamma=gamma)
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        
        error = m.mean_squared_error(y_pred,y_test)
        
        classifiers.append((C, gamma, error,y_pred, classifier))        
        
print(len(classifiers))


classifiers.sort(key = lambda x:x[2], reverse = False)
print(classifiers[0][3])
clf = classifiers[0][4]

from sklearn.externals import joblib
joblib.dump(clf, 'treinamento/treinamento.pkl') 
classif = joblib.load('treinamento/treinamento.pkl')

# Predicting the Test set results
# y_pred = classifiers[0][3]
y_pred = classif.predict(X_test)
print(X_test)

print(y_test[0:35])
print(y_pred[0:35])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

print(cm)





