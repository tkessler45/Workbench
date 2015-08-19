__author__ = 'tkessler'

import os, time, threading

"""
Pipes are declared as a sender and receiver pairing. This pairing can be applied to any number
of writers and readers. However, pipes are queues of sorts, where once read, data is popped off
so if not timed correctly, data in shared pipes may be lost for the intended process.
"""

(inpipe2, outpipe2) = os.pipe()
pipein, pipeout = os.pipe() #global pipe...replacing private one...accessed by forked parent and nonforked thread

def child(outpipe):
    num = 0
    while True:
        time.sleep(num)
        os.write(outpipe, "".join(["Message at time ",str(num)]).encode())
        #os.write(outpipe2, "".join(["Message to pipe2 at time ",str(num)]).encode())
        num = (num +1) % 5

def parent():
    #pipein, pipeout = os.pipe() #private pipe...
    if os.fork() == 0: #fork the current process and return ID....if 0, then its the child.
        child(pipeout)
    else:
        while True:
            line = os.read(pipein, 32)
            print("Parent received \"%s\" through the pipe..." % line)

def nonforked():
    print("thread started")
    while True:
        line = os.read(pipein, 1)
        print(": %s", line)

newthread = threading.Thread(target=nonforked)
newthread.start()
parent()