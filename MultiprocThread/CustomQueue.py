__author__ = 'tkessler'

class myfifo:
    data = []
    def push(self,var):
        self.data.append(var)
    def pop(self):
        return self.data.pop(0)

class myfilo:
    data = []
    def push(self,var):
        self.data.append(var)
    def pop(self):
        return self.data.pop(-1)

newfifo = myfifo()
newfifo.push("ASDF")
newfifo.push(123)

newfilo = myfilo()
newfilo.push("ASDF")
newfilo.push(234)

print(newfifo.pop())
print(newfifo.pop())

print(newfilo.pop())
print(newfilo.pop())