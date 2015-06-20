__author__ = 'tkessler'

import os, pprint
from sys import argv, exc_info


trace = 1
dirname, extname = os.curdir, '.py'
if len(argv) > 1: dirname = argv[1]
if len(argv) > 2: extname = argv[2]
if len(argv) > 3: trace - int(argv[3])

# printer that prints encoded string if unable to print raw...
def tryprint(str):
    try:
        print(str)
    except UnicodeEncodeError:
        print(str.encode())

visited = set()
allsizes = []

for (dirpath, dirnames, filenames) in os.walk(dirname):
    if trace: tryprint(dirpath)
    dirpath = os.path.normpath(dirpath)
    fixeddir = os.path.normcase(dirpath)
    if fixeddir in visited:
        continue
    else:
        visited.add(fixeddir)
        for file in filenames:
            if file.endswith(extname):
                if trace > 1: tryprint("+++"+file)
                fullpath = os.path.join(dirpath, file)
                try:
                    bytesize = os.path.getsize(fullpath)
                    lines = sum(+1 for line in open(fullpath, 'rb'))
                except Exception:
                    print('Error:', exc_info()[0])
                else:
                    allsizes.append((bytesize, lines, fullpath))

#This calls a recursive use of ('title','key') definition...
for (title, key) in [('bytes', 0), ('lines', 1)]:
    print('\nBy %s...' % title)
    a=lambda x: x[key]
    print(a((title,key)))
    allsizes.sort(key=lambda x: x[key]) #x for lambda is an instance of (title, key)
    pprint.pprint(allsizes[:3])
    pprint.pprint(allsizes[-3:])