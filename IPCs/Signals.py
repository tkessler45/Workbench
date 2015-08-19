__author__ = 'tkessler'

import sys, signal, time

"""
We are defining different signal handlers, one that can be assigned dynamically, and another that
is static.
"""

def now(): return time.ctime(time.time())

def sigHandler(signum, stackframe):
    print('got signal', signum, 'at', now())

def handler45(sig, stackframe): #sig receives the signal, and stackframe is required...
    print("AAAAAAHHHHHHH!!!!!!")

signum = int(sys.argv[1])
#Separate handlers for signals
signal.signal(signum, sigHandler) #this sets the action when the specific signal is received....
signal.signal(4, handler45) #tells handler45 to activate when signal is received

while True: signal.pause() #wait for any signal to be received...