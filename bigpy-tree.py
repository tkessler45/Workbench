__author__ = 'tkessler'

import sys, os, pprint
trace = False

path = input("Starting path:")
if not path:
    if sys.platform[:3]=='win': #alternative: sys.platform.startswith('win')
        path = r'C:\Python*\Lib'
    else:
        path = r'/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/'

filesizes = []

#start at directory
#recursively build list of files, filtering on .py
#for each file, append detected size

for (dirpath, dirnames, filenames) in os.walk(path, onerror=print):
    if trace: print(dirpath)
    for file in filenames:
        if file.endswith('.pxp'):
            filesizes.append((os.path.getsize(dirpath+os.sep+file),dirpath+os.sep+file))

filesizes.sort(reverse=True)
print(filesizes[:2])