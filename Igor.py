__author__ = 'tkessler'

import igorclasses as ig
import time
import matplotlib
from pylab import *

a = ig.pxp('/Users/tkessler/igortest.pxp')

plot(a.getwave('root','avef3').data)
time.sleep(10)