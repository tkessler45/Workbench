__author__ = 'tkessler'

"""
generated pipe will block on recv() until message sent through....

STEPS:
    1. create pipe-handling processes --> intended to receive a pipe end and send info through it
    2. generate pipe(s)
    3. start process or thread with the pipe handler, and pass pipe end(s) as arguments.
    4. Run processes to initiate pipe usage...
"""

import os, time
from multiprocessing import Process, Pipe

def sender(pipe):
    """
    send object to parent on anonymous multiprocessing pipe
    :param pipe:
    :return:
    """
    pipe.send(['spam']+[42,'eggs']) #arrays sent....as one combined
    pipe.close()

def talker(pipe):
    """
    send and receive via the passed pipe...
    :param pipe:
    :return:
    """
    pipe.send(dict(name="Bob",age=42))
    reply = pipe.recv()
    print("Talker got \"%s\" in reply" % reply)

if __name__ == "__main__":
    (endA, endB) = Pipe() #generate pipe
    Process(target=sender, args=(endB,)).start() #initiate function with process, using pipe end
        # will block here until pipe sends value...
    print('parent got:', endA.recv()) #print the local received value from pipe...
    endA.close()
    endB.close()
    print(endA, endB)

    (endA, endB) = Pipe() #generate pipe again
    childproc = Process(target=talker, args=(endB,))
    childproc.start()

    print('parent got: ', endA.recv())
    endA.send("message through the pipe")
    childproc.join()
    print('parent exit...')