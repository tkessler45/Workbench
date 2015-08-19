__author__ = 'tkessler'

import os, time, threading, sys, queue

"""
Pipes are declared as a sender and receiver pairing. This pairing can be applied to any number
of writers and readers. However, pipes are queues of sorts, where once read, data is popped off
so if not timed correctly, data in shared pipes may be lost for the intended process.
"""

fifofile = '/tmp/thefifo'
if not os.path.exists(fifofile):
    os.mkfifo(fifofile)

def producer():
    num = 0
    fifo_out = os.open(fifofile, os.O_WRONLY) #open the fifo for writing by the producer
    while True:
        time.sleep(num)
        #os.write(fifo_out, "".join(["Message  ",str(num)]).encode())
        os.write(fifo_out, "".join(["Message  ",str(num),"\n"]).encode()) #need \n for readline...
        num = (num +1) % 5

def consumer():
    fifo_in = open(fifofile, "r") #open for reading as string...
    #fifo_in = os.open(fifofile, os.O_RDONLY)
    while True:
        line = fifo_in.readline()[:-1] #read any available line on the fifo...
        #line = os.read(fifo_in, 24)
        print("Read: %s" % line)

#Thread the calls...
producerTH = threading.Thread(target=producer)
consumerTH = threading.Thread(target=consumer)
producerTH.start()
consumerTH.start()
