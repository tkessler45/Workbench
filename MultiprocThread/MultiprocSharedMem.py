__author__ = 'tkessler'

"""
The only variables updated by a process are shared memory mp variables such as:
    mp.Array --> Lists...
    mp.Value --> single entities...

When we create a new process, all variables of the current process are copied to the new process as-is. Shared
memory objects are copied as a link/pointer to the same memory address, allowing them to be updated by any of
the processes, but across all processes...
"""

import multiprocessing as mp
import os, time

procs = 3
count = 0

def showdata(label, val, arr):
    """
    print data values...
    :param label:
    :param val:
    :param arr:
    :return:
    """
    print(label, "==> PID:", os.getpid(), ", count:", count, ", int:", val.value, ", arr:", list(arr))

def updater(val, arr):
    """
    communicate via shared memory...
    :param val:
    :param arr:
    :return:
    """
    global count  #not updated when called from a new process....
    count+=1
    val.value+=1  #updated when called from a mp process, if "val" is an mp variable...
    for i in range(3): arr[i] += 1

if __name__=="__main__":
    #shared memory objects...
    scalar = mp.Value('i', 0) #integer...
    vector = mp.Array('d', procs) #double...

    showdata('parent start', scalar, vector)

    p = mp.Process(target=updater, args=(scalar, vector)) #count will not update (not accessible from mp process)
    p.start()
    p.join() # block the main thread until "p" process is complete...
    showdata('parent start', scalar, vector)
    updater(scalar,vector) # count will update, since it is local...
    showdata('parent start', scalar, vector)

    print('\nloop1 (updates in parent, serial children)...')
    for i in range(procs):
        #update values first...
        count+=1 #only updated because iteration is local....
        scalar.value+=1
        vector[i]+=1
        #display value updates immediately using child procs...
        p=mp.Process(target=showdata, args=(('process %s' %i), scalar, vector))
        p.start();p.join()

    print('\nloop2 (updates in parent, parallel in children)...')
    ps = [] #array for process management...
    for i in range(procs):
        count+=1 #global updated incrementally--updated once then copied as-is to each process
        scalar.value+=1 #mp shared memory updated at each iteration...overall 3x and shared to all processes.
        vector[i]+=1
        #create and start child processes to show data
        p=mp.Process(target=showdata, args=(('process %s' % i), scalar, vector))
        #
        p.start()
        ps.append(p) #tag running process to ps array...should all be running in parallel
        # all variables updated before showdata in each process can run
        time.sleep(.1) # ...a delay should stop that...
    for p in ps: #processes in array...all updated
        p.join()

    print('\nloop3 (updates in serial children)...')
    for i in range(procs):
        p = mp.Process(target=updater, args=(scalar,vector)) #count not updated in this process, as it
        p.start()
        p.join()
        showdata('the data from parent', scalar, vector)

    print('\nloop4 (updates in parallel children...')
    for i in range(procs):
        p = mp.Process(target=updater, args=(scalar,vector))
        p.start()
        ps.append(p)
    for n in ps:
        n.join()
        showdata('parent end', scalar, vector)