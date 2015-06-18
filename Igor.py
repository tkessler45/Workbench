__author__ = 'tkessler'

import igorclasses as ig
import time
import matplotlib
from pylab import *
import threading as th
import queue

thequeue = queue.Queue()

def loader(fp, q):
    assert type(q)==queue.Queue
    q.put(ig.pxp(fp))
    print(fp,"loaded...")

list = ['/Users/tkessler/igortest.pxp','/Users/tkessler/igortest2.pxp','/Users/tkessler/igortest3.pxp']

threads = []
filelist = []

for file in list:
    threads.append(th.Thread(target=loader, args=(file, thequeue)))

#print(threads)
#print(filelist)

for t in threads:
    t.start()

print(thequeue.qsize())
thequeue.join()

print("main thread exiting")