import pandas as pd
from numpy import *


data = pd.read_csv('./rssiData5.csv',header=None)
print("Data")
print(data)
print("X_train")
print(data.iloc[1:, :5].values)
print(type(data.iloc[1:, :5].values))
print("y_train")
print(data.iloc[1:, 5].values)
print(type(data.iloc[1:, 5].values))
print("Wifi1:")
print(data.iloc[0,0])
print(type(data.iloc[0,0]))
print("Wifi2:")
print(data.iloc[0,1])
print("Wifi3")
print(data.iloc[0,2])
print("Wifi4:")
print(data.iloc[0,3])
print("Wifi5:")
print(data.iloc[0,4])
wifiName = data.iloc[0,0] + "," + data.iloc[0,1] + "," + data.iloc[0,2] + "," + data.iloc[0,3] + "," + data.iloc[0,4]
print(wifiName)