__author__ = 'tkessler'

class UnknownCommand(Exception): pass #new custom Exception class...fully inherited

class filescan:

    def __init__(self, thefile):
        self.thefile = thefile

    def thescanner(self, datafile, function):
        for line in open(datafile,"r"):
            function(line)

    def subfirst(self, thestr):
        if thestr[0]=="*":
            print("Ms. "+thestr[1:])
        elif thestr[0]=="+":
            print("Mr. "+thestr[1:])
        else:
            raise UnknownCommand(thestr)

class filefilter:
    def __init__(self,thefile="",thefunc="",*args):
        self.thefile = thefile
        self.thefunc = thefunc
        self.inargs = args

    def doit(self):
        infile = open(self.thefile, 'r')
        outfile = open("_new.".join(infile.name.split(".")),"w")
        for line in infile:
            outfile.write(self.thefunc(line, self.inargs[0],self.inargs[1]))
        outfile.close()
        infile.close()
        #run the filter

    def replacechars(instr, *args):
        print(args)
        return instr.replace(args[1],args[2])


