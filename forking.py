__author__ = 'tkessler'

import os

def child():
    print("This is the child process:", os.getpid())
    os._exit(0)

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print("Parent and child PIDs are", os.getpid(), newpid)
        if input() == 'q': break

if __name__ == "__main__":
    parent()