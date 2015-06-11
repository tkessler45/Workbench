__author__ = 'tkessler'

import threading, time

"""
We build a subclass of the threading Thread, and replace the run
function to target a local function passed in as an argument.
"""
#with subclass
class threadObject(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.func(self.args)

#without subclass
def threadedfunction(var):
    time.sleep(1)
    print("    Thread running...")
    time.sleep(1)
    thefile = open('testfile.txt','w')
    thefile.write("zZZZZzzZZZzzzzZZZ")
    thefile.close()
    print(var)

newthread = threadObject(threadedfunction, "    Thread finished...")
"""
daemon true requires external timing...otherwise program will wait
for it to finish. Child thread as a d
"""
newthread.setDaemon(False) #False = user thread (non-daemon)
newthread.start()

#time.sleep(2)
if not newthread.isDaemon():
    print("Non-Daemon thread detected")
    print("This should keep the program from quitting")
    print("Waiting for non-daemon thread to finish")
else:
    print("Daemon thread detected")
    print("This should not keep the program from quitting")
    print("Main thread finished....daemon thread halted")