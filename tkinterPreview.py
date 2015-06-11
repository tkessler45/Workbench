__author__ = 'tkessler'

from tkinter import Tk
from tkinter.messagebox import showinfo

def displaywarning():
    showinfo("Wahoo title", "wahoo message")

mainwin = Tk() #main TK loop...
mainwin.after(5500, displaywarning) # displaywarning provides fn name only...
#mainwin.after(5500, displaywarning()) # displaywarning() calls displaywarning immediately
#mainwin.after(5500, showinfo("Wahoo title", "wahoo message")) # showinfo() calls showinfo immediately
mainwin.mainloop()