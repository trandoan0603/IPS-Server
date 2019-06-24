from tkinter import *
import time
import random

class Bong:
    def __init__(self,canvas,color):
        self.canvas =canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,100,200)
    def draw(self):
        print("go")
        self.canvas.coords(self.id,100,100,100,100)
tk = Tk()
tk.resizable(0,0)
can = Canvas(tk,width = 400, height = 500)
can.pack()

bong = Bong(can,"red")

while 1:
    bong.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(5)