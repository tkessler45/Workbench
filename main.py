__author__ = 'tkessler'

from classes import *
import _thread

#a = filescan('data.txt')
#a.thescanner(a.thefile, a.subfirst)

#a = filefilter('infile.txt', filefilter.replacechars,"W","X")
#a.doit()
#_thread.start_new_thread(a.makeafile, ("/Users/tkessler/PycharmProjects/Workbench/filename.txt",))

# b = filefilter()
# b.thefile="infile.txt"
# b.thefunc=b.replacechars
# b.
#b.thefile('infile.txt')


def stage1():
    tmp=1
    def stage2():
        def stage3():
            print('stage3 %d' % tmp)
        print('stage2 %d' % tmp)
        stage3()
    print('stage1 %d' % tmp)
    stage2()

stage1()