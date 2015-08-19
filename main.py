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

print("YAY")

# def stage1():
#     tmp=1
#     def stage2():
#         def stage3():
#             print('stage3 %d' % tmp)
#         print('stage2 %d' % tmp)
#         stage3()
#     print('stage1 %d' % tmp)
#     stage2()
#
# stage1()

def fizzbuzz(intList):
    outlist=[]
    for item in intList:
        if item%3==0 and item%5==0:
            outlist.append('Fizz')
        elif item%5==0:
            outlist.append('Buzz')
        elif item%3==0:
            outlist.append('FizzBuzz')
        else:
            outlist.append(item)
    return outlist

print(fizzbuzz(range(1,31)))
