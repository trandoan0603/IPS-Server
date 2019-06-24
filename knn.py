import numpy as np
from sklearn import neighbors
import pandas as pd


data = pd.read_csv('./trainData.csv', header = None)

#print(data.head(14))

X_train = data.iloc[:,:-1].values
y_train = data.iloc[:,3].values


#print(X_train)
#print(y_train)

def knn():
    clf = neighbors.KNeighborsClassifier(3)
    clf.fit(X_train,y_train)
    b = [[55,56,57]]
    #test = pd.read_csv('./teraterm1.csv',header=None)
    #print(test.tail(1))
    #X_test = test.tail(1)
    print(b)
    y_pre = clf.predict(b)
    print(y_pre)
    return (y_pre)

#knn()

def knn1(a):
    list = a
    #print(a)
    clf = neighbors.KNeighborsClassifier(3)
    clf.fit(X_train,y_train)

    #test = pd.read_csv('./teraterm1.csv',header=None)
    #print(test.tail(1))
    #X_test = test.tail(1)

    #print(list)
    y_pre = clf.predict(list)
    print(y_pre)
    return y_pre


