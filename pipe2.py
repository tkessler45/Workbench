__author__ = 'tkessler'

import os, time, threading

def child(output):
    num = 0
    while True:
        time.sleep(num)
        os.write(output, "This ends in a line terminator\n".encode()) #the \n terminator is required...
        num = (num+1) % 5

breakflag=False

def switch():
    global breakflag
    while True:
        if input()=="d":
            breakflag = True

thethread=threading.Thread(target=switch)
thethread.setDaemon(True)

def parent():
    global breakflag
    (pipein, pipeout) = os.pipe()
    if os.fork() == 0:
        os.close(pipein)
        child(pipeout)
    else:
        os.close(pipeout)
        pipefile = os.fdopen(pipein)
        while True:
            if breakflag:
                break
            else:
                pipeline = pipefile.readline()[:-1] # reads a line without the terminating character, so the read is blocked...requires pipe to supply termination character.
                print("Message from child is: %s" % pipeline)

thethread.start()

parent()
