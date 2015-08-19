__author__ = 'tkessler'

from tkinter import *
from math import *
from scipy import stats

class CartCanvas(Canvas):
    """
    Take the canvas element input, provide conversion of output from origin
        cvs = None -- input object (tkinter canvas)
        origin = (%,%) -- origin coordinates based on canvas size
    """
    def __init__(self, parent=None, origin=(0,0), **Options):
        Canvas.__init__(self, master=parent, **Options)
        self.pack()
        self.origin = origin
        self.width = float(self.config().get('width')[4]) #replace with passed 'width', etc.?
        self.height = float(self.config().get('height')[4])

    def x(self,n):
        return self.origin[0]*self.width+n

    def y(self,n):
        return self.height-(n+self.origin[1]*self.height)

class Graph(CartCanvas):
    """
    Accept function and graph it by line segments...
    TODO: adjust range when origin is (0.1, 0.1)....
        decouple x from width...
    """
    def __init__(self, res=(1,1), step=float(1), **Options):
        CartCanvas.__init__(self, **Options)
        self.pack()
        self.xres=res[0]
        self.yres=res[1]
        self.step = step
        self.xstart = int(-self.origin[0]*self.width)
        self.xend = int(self.origin[0]*self.width)
        self.xrange = range(self.xstart,self.xend,int(self.step))

    def plotfn(self, fn):
        x=[n for n in self.xrange]
        for n in x:
            self.create_line(self.x(n*self.xres),self.y(fn(n)*self.yres),self.x((n+self.step)*self.xres),self.y((fn(n+self.step))*self.yres))

    def point(self,x,y):
        self.create_line(self.x(x)*self.xres-4,self.y(y)*self.yres,self.x(x)*self.xres+4,self.y(y)*self.yres)
        self.create_line(self.x(x)*self.xres,self.y(y)*self.yres-4,self.x(x)*self.xres,self.y(y)*self.yres+4)
    def plotxy(self,x,y):
        i=0
        for n in x:
            self.point(x[i],y[i])
            i+=1

class ScrolledGraph(Frame):
    def __init__(self, parent=None, **Options):
        Frame.__init__(self, master=parent, **Options)
        self.pack(expand=YES, fill=BOTH)
        grph = Graph(parent=self, origin=(0.5,0.5), width=500, height=500, res=(1,1), step=float(1))
        grph.config(width=500, height=500)
        grph.config(scrollregion=(0,0,-1000,1000))
        grph.pack(side=LEFT, expand=YES, fill=BOTH)
        sbar = Scrollbar(self)
        sbar.config(command=grph.yview)
        grph.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        grph.plotfn(self.gfn)
    def gfn(self, x):
        return sin(x/10)

#cvs.create_line(ox*w,h-oy*h,100+ox*w,h-(100+oy*h))
root = Tk()
#g = Graph(parent=root, origin=(0.5,0.5), width=500, height=500, res=(1,1), step=float(1))#, bg='white')
#g.pack()
s = ScrolledGraph(root)
s.pack()

def gnorm(x):
    return 1/float(sqrt(2*pi)*e**((x**2)/2))
#g.plotfn(gnorm)
x = [n-250 for n in range(500)]
y = [stats.expon.rvs() for n in range(500)]
#g.point(0,0)
#g.point(100,100)
#g.plotxy(x,y)
#g.plotxy([0,1,2,4,8,10,20,40,80,160,320],[0,50,100,150,200,250,300,350,400,450,500])



# c.create_line(c.x(-100),c.y(100),c.x(100),c.y(10))
# c.create_line(c.x(0),c.y(0),c.x(100),c.y(20))
# c.create_line(c.x(0),c.y(0),c.x(100),c.y(40))
# c.create_line(c.x(0),c.y(0),c.x(100),c.y(80))

root.mainloop()

# for i in range(10):
#     cvs.create_line(xstart,ystart,xend,yend)‰