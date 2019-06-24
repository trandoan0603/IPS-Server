#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from sklearn import neighbors
import json
import pandas as pd
from numpy import *
#from knn import *



'''data = pd.read_csv('./trainData.csv', header = None)
#print(data.head(14))
X_train = data.iloc[:,:-1].values
y_train = data.iloc[:,3].values
clf = neighbors.KNeighborsClassifier(3)
clf.fit(X_train,y_train)'''

data = pd.read_csv('./trainData1.csv',header=None)
X_train = data.iloc[1:,:3].values
y_train = data.iloc[1:,3].values
clf = neighbors.KNeighborsClassifier(3)
clf.fit(X_train,y_train)

wifiName = data.iloc[0,0] + "," + data.iloc[0,1] + "," + data.iloc[0,2]


#db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)



def knn1(a):
    list = a
    y_pre = clf.predict(list)
    print(y_pre)
    return y_pre


class Hello(Resource):
    def post (self):
        '''a = int(request.form['data1'])
        b = int(request.form['data2'])
        c = int(request.json['data3'])'''
        a = request.json
        a = json.loads(a)
        print(a)
        print(a["a"])
        print(a["b"])
        print(a["c"])
        d = [[a["a"],a["b"],a["c"]]]
        print(d)

        '''json_dump = json.dumps({'a': knn1(d)},cls = NumpyEncoder)
        print(json_dump)
        n = str(json_dump)
        print(n)
        print(type(n))'''
        return {"a":str(knn1(d))}
    '''def get(self):
        return knn(a)'''

    def get (self):
        return wifiName

api.add_resource(Hello, '/hello')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
