from tkinter import *
from time import sleep
from sklearn import neighbors
import pandas as pd
from findXY import *


data = pd.read_csv('./trainData.csv', header = None)

#print(data.head(14))

X_train = data.iloc[:,:-1].values
y_train = data.iloc[:,3].values
clf = neighbors.KNeighborsClassifier(3)
clf.fit(X_train, y_train)

#print(X_train)
#print(y_train)

def knn2():
    #b = [[55,56,57]]
    test = pd.read_csv('./teraterm1.csv',header=None)
    #print(test.tail(1))
    X_test = test.tail(1)
    #print(b)
    y_pre = clf.predict(X_test)
    #print(y_pre)
    return (y_pre)


tk = Tk()
tk.title("Dinh vi trong nha")
tk.resizable(0,0)

class Point:
    def __init__(self,canvas,x,y):
        self.x = x
        self.y = y
        self.canvas=canvas
        self.id = canvas.create_oval([x - 10, y + 10], [x + 10, y - 10], fill="red")
    def draw(self,x,y):
        self.x = x
        self.y = y
        self.canvas.coords(self.id,self.x - 10, self.y + 10, self.x + 10, self.y - 10)
    def change1(self):
        self.canvas.itemconfig(self.id,fill="white")
    def change2(self):
        self.canvas.itemconfig(self.id,fill="red")

can = Canvas(tk, width = 1000, height = 500)
can.create_rectangle([150,350],[850,150],outline = "black",width=3)
can.create_line([250,150],[250,350],width=3)
can.create_rectangle([425,350],[625,225],outline = "black",width=3)
can.create_rectangle([625,350],[700,250],outline = "black",width=3)
can.pack()

point = Point(can,findX(knn2()),findY(knn2()))


while 1:
    point.draw(findX(knn2()), findY(knn2()))
    print(knn2())
    sleep(0.5)
    for n in range (0,2,1):
        point.change1()
        tk.update_idletasks()
        tk.update()
        sleep(1)
        point.change2()
        tk.update_idletasks()
        tk.update()
        sleep(1)


