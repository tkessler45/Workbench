__author__ = 'tkessler'

import igorclasses as ig
from pylab import *
import time

a = ig.pxp('/Users/tkessler/igortest.pxp')

w = a.getwave('root:imem4') #'root:Nest1:Nest2:test'
#open('wavetext.txt','w').write(a.__str__())
#print("the wave is type:",type(w))
x = ig.wave(w)
#x.wavestats()

#plot(x.data)

##time.sleep(5)

# print(x.sum())
# print(x.mean())
# print(x.var())
# print(x.sdev())
# print(x.sem())
# print(x.rms())

print(a.folders())
x.wavestats()
