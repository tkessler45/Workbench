__author__ = 'tkessler'

import pickle

class anobject():
    def __init__(self, var1=0, var2=0):
        self.var1=var1
        self.var2=var2
        self.arr=[]

    def appendSelfEval(self):
        self.var1+=1
        self.var2+=1
        self.arr.append(self.var1+self.var2)

    # def __repr__(self):
    #     print("wahoo")

    def save(self,fp):
        pickle.dump(self,fp)

def main():
    a = anobject()
    b = anobject()

    for i in range(10):
        a.appendSelfEval()

    b.appendSelfEval()

    print(a.arr)
    print(b.arr)

    repr(a)

    file1 = open('pickle1','wb')
    file2 = open('pickle2','wb')

    # pickle.dump(a,file1)
    # pickle.dump(b,file2)
    a.save(file1)
    b.save(file2)

    file1.close()
    file2.close()

    for i in range(5):
        a.appendSelfEval()
        b.appendSelfEval()

    c = pickle.load(open('pickle1', 'rb'))
    d = pickle.load(open('pickle2', 'rb'))

    print("------\n")
    print(a.arr)
    print(b.arr)
    print(c.arr)
    print(d.arr)
    print("------\n")
    c.appendSelfEval()
    d.appendSelfEval()
    print(c.arr)
    print(d.arr)

if __name__=="__main__":
    main()