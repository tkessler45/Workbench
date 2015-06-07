__author__ = 'tkessler'

import os

def child():
    print("This is the child process:", os.getpid()) #gets current PID from parent process...
    os._exit(0) #exits itself (PID 0)...

def parent():
    while True:
        newpid = os.fork() #returns 0 to child process, and both processes run!!
        print(newpid)
        if newpid == 0: #if 0, then we are the child...
            child() #this will print (above) and exit (pid 0)
        else:
            print("Parent and child PIDs are", os.getpid(), newpid)
        if input() == 'q': break

parent()