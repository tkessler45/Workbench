__author__ = 'tkessler'

numconsumers = 2 # how many consumers to start
numproducers = 4 # how many producers to start
nummessages = 4 # messages per producer to put

import _thread, queue, time, threading

safeprint = threading.Lock() #_thread.allocate_lock() # else prints may overlap

theQueue = queue.Queue() # shared global, infinite size

# regularly place data in the global queue...
def producer(idnum, dataQueue): #similar to a GUI input...like a loader...or background process...
    #may load data onto the data queue for later handling by lists...
    #usually reserved for non-GUI processing tasks.
    #can place callback (updating) function in the queue...
    for msgnum in range(nummessages):
        time.sleep(idnum) #progressive wait time for data insertion on queue
        dataQueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))

def consumer(idnum, dataQueue): #similar to a GUI output...like a list view for loaded data...
    #may load data from queue into a list view for management....
    #usually reserved for main GUI thread...
    while True:
        time.sleep(0.1)
        try:
            data = dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            #with safeprint: #ensure thread has exclusive access to stdout
                print('consumer', idnum, 'got =>', data)

if __name__ == '__main__': #simulated interaction between loaders and handlers...
    #similar to retrieval of data from button press queues
    for i in range(numconsumers):
        thread = threading.Thread(target=consumer, args=(i, theQueue))
        thread.setDaemon(True)
        thread.start()
        #_thread.start_new_thread(consumer, (i,))
    waitfor = []
    for i in range(numproducers):
        #_thread.start_new_thread(producer, (i,))
        thread2 = threading.Thread(target=producer, args=(i, theQueue))
        waitfor.append(thread2)
        thread2.start()

    #time.sleep(((numproducers-1) * nummessages) + 1)
    for thread in waitfor: thread.join()
    print('Main thread exit.')