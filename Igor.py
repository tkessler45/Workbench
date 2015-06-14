__author__ = 'tkessler'

import igorclasses as ig
import pprint
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

ig.checktype('var',['dict'])

pprint.pprint(a.folders())

pprint.pprint(a.folderinfo("root:globals")[:2])
#x.wavestats()
