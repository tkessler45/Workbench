__author__ = 'tkessler'

"""
Multiprocessing example...
    - Each process starts with the name __main__
    - Each process has a separate PID
"""

import os
from multiprocessing import Process, Lock

def whoami(label, lock):
    msg = '%s: name:%s, pid:%s'
    with lock:
        print(msg % (label,__name__,os.getpid()))

if __name__ == '__main__':
    lock = Lock() #instantiate multiprocessing lock object
    whoami('function call', lock) #lock our resource baton for individual processes

    p = Process(target=whoami, args=('child process', lock))
    p.start()
    p.join() # wait for process to receive baton and complete before terminating...

    for i in range(5):
        Process(target=whoami, args=(('Spawned process %d',i),lock)).start()

    with lock: #last command waits for baton to be free...
        print('Main process exit.')