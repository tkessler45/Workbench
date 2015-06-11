__author__ = 'tkessler'

"""
In this program we are managing access to a set of data through the
fifo-like access for items in a data queue. We are creating four data
creator threads that each put a message on the queue.
"""

datausers = 2
datacreators = 4
nmessages = 5

import _thread, queue, time

globallock = _thread.allocate_lock()
theQueue = queue.Queue()

def creator(id):
    for msg in range(nmessages):
        time.sleep(id)
        theQueue.put('message %d from creator %d' % (msg, id))

def user(id):
    while True:
        time.sleep(0.1)
        try:
            data = theQueue.get(block=False)
        except queue.Empty:
            print("user %d detects empty queue" % id)
        else:
            with globallock:
                print('user %d got %s' % (id, data))

if __name__ == '__main__':
    for i in range(datacreators):
        _thread.start_new_thread(user, (i,))
    for i in range(datacreators):
        _thread.start_new_thread(creator, (i,))
    time.sleep(((datacreators-1)*nmessages)+1)
    print("main thread exit")