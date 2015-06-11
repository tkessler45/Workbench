__author__ = 'tkessler'

from classes import *
import _thread

#a = filescan('data.txt')
#a.thescanner(a.thefile, a.subfirst)

a = filefilter('infile.txt', filefilter.replacechars,"W","X")
#a.doit()
_thread.start_new_thread(a.makeafile, ("/Users/tkessler/PycharmProjects/Workbench/filename.txt",))

# b = filefilter()
# b.thefile="infile.txt"
# b.thefunc=b.replacechars
# b.
#b.thefile('infile.txt')


