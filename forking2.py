__author__ = 'tkessler'

import os, time
from scipy import stats

# def timecounter(count):
#     #os.execv('/usr/bin/open','-n','Calculator')
#     print("PID %s (number %s) launching Calculator..." % (os.getpid(),count))


for n in range(5):
    PID = os.fork()
    if PID == 0: #the child...
        print("This child's PID is: %s" % os.getpid())
        # os.popen('open -n -a Calculator')
        # os.execlp('open','-n','-a','Calculator')
        # timecounter(n) #child does stuff...

        # os.popen('logger '+str(os.getpid()))
        os.execlp('logger','logger',str(os.getpid()))
        # timecounter(n) #child does stuff...

        os._exit(0) #child process ends itself when done, to prevent recursion...
    else:
        print("new child forked: %d" % PID)
