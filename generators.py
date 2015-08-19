__author__ = 'tkessler'

import itertools
import operator

def main():
    gen = (x*x for x in range(3))
    for i in gen:
        print(i)

def creategen(n):
    print("ASDFASDF")
    for num in range(n):
        yield num*10

newgen = creategen(5) # creates generator function
anothergen = creategen(10)
print('wwwww')
newgen.__next__()
for i in newgen:
    print(("newgen called..."))
    for n in anothergen:
        print(n)
    print(i)

# print("--------------")
# for i in newgen:
#     print(i)
# print("--------------")
# print(newgen.gi_running)
# print("--------------")
# for i in anothergen:
#     print(i)