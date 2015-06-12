__author__ = 'tkessler'

import threading, time

#create batons (locks)
thebaton = threading.Lock()
secondlock = threading.Lock()

"""
Declared file locks such as firstlock and secondlock above are arbitrary, and can be used anywhere. Resources are only
locked if a specific lock is declared in the code below, and then that specific lock is again used elsewhere. When next
called, the lock will provide a block for the resources it is attempting to lock. Therefore firstlock called in afunc
will block bfunc provided
"""

def afunc(var):
    #time.sleep(1)
    with thebaton: #Ask for baton. Only run following code if available. Wait if not available.
        for i in range(5):
            time.sleep(.0002)
            time.sleep(1)
            print(var)

def bfunc(var):
    #time.sleep(1)
    #with secondlock:
    with thebaton: #attempt to hold the baton, if available
        print(var)

a=threading.Thread(target=afunc, args=(5,))
b=threading.Thread(target=bfunc, args=(6,))
c=threading.Thread(target=afunc, args=(7,))
d=threading.Thread(target=bfunc, args=(8,))
a.start() #trigger a baton hold on afunc
b.start() #trigger a baton hold request, but afunc may still be holding it (must wait)
c.start() #again attempt a baton hold request...must wait for prior baton holds...
d.start() #



