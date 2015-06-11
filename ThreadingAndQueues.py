__author__ = 'tkessler'

import _thread, time, queue

def child(threadid):
    while True:
        print("This child thread ID is: ", threadid)
        time.sleep(2)


def startthread():
    tid = 0
    while True:
        print(_thread.start_new_thread(child, (tid,)))
        tid = input("New TID:")
        if tid == "q": break

class newclass:
    def __init__(self, num):
        self.num = num
    def action(self):
        r = open('testfile.txt','w')
        while not thequeue.empty():
            r.write(thequeue.get(block=False))
            thequeue.task_done()
        r.close()

#startthread()

thequeue = queue.Queue()
thequeue.put("First item on queue\n")
thequeue.put("Second item on queue\n")
thequeue.put("Third item on queue")

aclass = newclass
_thread.start_new_thread(aclass.action, (None,))

thequeue.join()
print("Exiting...")