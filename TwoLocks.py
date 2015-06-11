__author__ = 'tkessler'

import threading, time

firstlock = threading.Lock()
secondlock = threading.Lock()

def afunc(var):
    #time.sleep(1)
    with firstlock:
        for i in range(5):
            time.sleep(.0002)
            print(var)

def bfunc(var):
    #time.sleep(1)
    #with secondlock:
        print(var)

a=threading.Thread(target=afunc, args=(5,))
b=threading.Thread(target=bfunc, args=(6,))
c=threading.Thread(target=afunc, args=(7,))
d=threading.Thread(target=bfunc, args=(8,))
a.start()
b.start()
c.start()
d.start()



