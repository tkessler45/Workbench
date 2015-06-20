__author__ = 'tkessler'

import os, glob, sys
dir = r'/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4' if len(sys.argv) == 1 else sys.argv[1]
ftype = 'py'
#print("path: %s" % dir+os.sep+"*.py")

allsizes = []
if os.path.exists(dir):
    allftype= glob.glob(dir+os.sep+'*.'+ftype) #get list...
    for file in allftype:
        filesize = os.path.getsize(file)
        allsizes.append((filesize, file)) #append tuple...

    allsizes.sort(reverse=True)
    for item in allsizes[:2]:
        print(str(item[0])+": "+item[1])
    print('...')
    for item in allsizes[-2:]:
        print(str(item[0])+": "+item[1])
else:
    print('path (%s) does not exist' % dir)
