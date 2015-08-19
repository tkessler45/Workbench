__author__ = 'tkessler'

import time
import _thread
import math

countmax = 3

def counter(id, count):
    for i in range(count):
        time.sleep(1)
        lockobj.acquire()
        print('[%s] => %s' % (id, i)) #
        lockobj.release()
    #lockarray[id].acquire()
    flagarray[id]=1
    print(flagarray)

lockobj = _thread.allocate_lock() # lock object...

#lockarray = [_thread.allocate_lock() for item in range(5)]
flagarray = [0 for n in range(countmax)]

for i in range(countmax):
    _thread.start_new_thread(counter, (i,countmax))

#time.sleep(3) # timing check to ensure thread does not exit before finished...
#for lock in lockarray:
#    while not lock.locked(): pass

#for flag in flagarray:
#    while not 0: pass

while round(math.fsum(flagarray)) < countmax:
    pass

print("main thread exiting...")