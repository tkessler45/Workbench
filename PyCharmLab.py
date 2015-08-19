__author__ = 'tkessler'

from pylab import *

def onpick(event): print('WAHOO')

f1 = figure()
f1s1 = f1.add_subplot(111)
f1s1.set_title('TEST')
f1s1d1 = f1s1.plot([1,2,3,2,4,3],'o', picker=5)
f1.canvas.mpl_connect('pick_event', onpick)
f1.show()