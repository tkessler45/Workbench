__author__ = 'tkessler'

import scipy
from matplotlib import pyplot
import matplotlib
import threading
from tkinter import *

def display():
    win = Tk()
    quitbutton = Button(win, text="Display", command=launchgraph)
    quitbutton.pack()
    win.mainloop()

def launchgraph():
    threading.Thread(target=plotit).start()

def plotit():
    print('wahoo')
    pyplot.plot([1,2,3,4,5,2,3,4,3,2,5])

if __name__=="__main__":
    display()
