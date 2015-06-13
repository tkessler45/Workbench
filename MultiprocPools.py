__author__ = 'tkessler'

"""
If you want to perform the same task on a set of objects, pool it
    - this will multi-process them...
"""

import os
import multiprocessing as mp

def powers(x):
    return 2 ** x

if __name__=="__main__":
    workers = mp.Pool(5)

    results = workers.map(powers,[1,2,3,4,5])
    print(results)