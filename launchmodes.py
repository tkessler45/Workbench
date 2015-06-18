__author__ = 'tkessler'

import sys, os
pyfile = (sys.platform[:3]=='win' and 'python.exe') or 'python'
pypath = sys.executable

def fixWindowsPath(cmdline): #cmdline is the path and command...
    splitline = cmdline.lstrip().split(' ') #array of elements by spaces...
    fixedpath = os.path.normpath(splitline[0]) #fix the path (first) element of the array...
    return ' '.join([fixedpath] + splitline[1:]) #reassemble path and the command...

class LaunchMode:
    #base class...announces instance and runs
    def __init__(self, label, command):
        self.what = label
        self.where = command

    def __call__(self, *args, **kwargs):
        self.announce(self.what) #call class function...
        self.run(self.where) # pass input command to the run function...

    def announce(self, text): #announcement function...
        print(text)

    def run(self, cmdline):
        assert False, 'run must be defined' #this class does not run anything...this will be overridden in inheritance...

class System(LaunchMode): #inherit the main launcher class for auto announcement
    def run(self, cmdline): #override main class run function to perform the desired action...
        cmdline = fixWindowsPath(cmdline)
        os.system('%s %s' % (pypath, cmdline))

class Popen(LaunchMode):
    def run(self, cmdline):
        cmdline = fixWindowsPath(cmdline)
        os.popen(pypath+' '+cmdline)

class Fork(LaunchMode):
    def run(self, cmdline):
        assert hasattr(os, 'fork')
        cmdline = cmdline.split()
        if os.fork()==0: # fork it and if the current return process is 0 (the child)...
            os.execv(pypath, [pyfile] + cmdline)

class StartArgs(LaunchMode): #win only...
    def run(self, cmdline):
        assert sys.platform[:3] == "win"
        os.system('start '+cmdline)

class Spawn(LaunchMode):
    def run(self, cmdline):
        os.spawnv(os.P_DETACH, pypath, (pyfile, cmdline))

class Top_level(LaunchMode):
    def run(self, cmdline):
        assert False, 'Sorry - mode not yet implemmented'

if sys.platform[:3]=='win':
    PortableLauncher = Spawn
else:
    PortableLauncher = Fork

class QuietPortableLauncher(PortableLauncher):
    def announce(self, text): # clear the announce for platform-dependent Fork or Spawn classes defined above...
        pass

def selftest():
    file = 'echo.py'
    input('default mode...')
    launcher = PortableLauncher(file, file)
    launcher()

    input('system mode...')
    System(file, file)() #label and command for the launcher are "file" and "file"...('echo.py')...

    if sys.platform[:3] == 'win':
        input('DOS start mode...')
        StartArgs(file,file)()

if __name__ == '__main__': selftest()