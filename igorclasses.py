__author__ = 'tkessler'

"""
packed.load('filename') object structure:

    [0]: [] -- raw array of all data objects
    [1]: { -- data structure
        root: {
            b'wavename1': WaveRecord
            b'wavename2': WaveRecord
            ...
            b'varname1': var
            b'varname2': var
            ...
            b'strname1': b'str'
            b'strname2': b'str'
            b'foldername1': {
                b'wavename1': WaveRecord
                b'wavename2': WaveRecord
                ...
                b'varname1': var
                b'varname2': var
                ...
                b'varname1': var
                b'varname2': var
            }
        }
    }

WaveRecord object structure:

    .wave: {
        version: val, -- wavemetrics wave format version?
        wave: {
            bin_header: {
                checksum: val,
                dataEUnitsSize: 0,
                dimEUnitsSize: array([0, 0, 0, 0]),
                dimLabelsSize: array([0, 0, 0, 0]),
                formulaSize: 0,
                noteSize: 0,
                optionsSize1: 0,
                optionsSize2: 0,
                sIndicesSize: 0,
                wfmSize: 8328,
            }
            data_units: b'',
            dimension_units: b'',
            formula: b'',
            labels: [[], [], [], []],
            note: b'',
            sIndices: array([], dtype=float64),
            wData: array([ 0.19195557,  0.19317627,  0.19195557, ...,  0.19378662]),
            wave_header: {
                aModified: 0,
                bname: b'fbndf3',
                botFullScale: -10.0,
                creationDate: 3487567867,
                dFolder: 51436672,
                dLock: 0,
                dataEUnits: 0,
                dataUnits: array([b'', b'', b'', b''], dtype='|S1'),
                depID: 81,
                dimEUnits: array([0, 0, 0, 0]),
                dimLabels: array([0, 0, 0, 0]),
                dimUnits: array([[b's', b'', b'', b''],
                                 [b'', b'', b'', b''],
                                 [b'', b'', b'', b''],
                                 [b'', b'', b'', b'']], dtype='|S1'),
                fileName: 0,
                formula: 0,
                fsValid: 0,
                kindBits: b'\x00',
                modDate: 3487567867,
                nDim: array([1001,    0,    0,    0]),
                next: 487179080,
                npnts: 1001,
                sIndices: 0,
                sfA: array([ 0.005,  1.   ,  1.   ,  1.   ]),
                sfB: array([ 25.105,   0.   ,   0.   ,   0.   ]),
                srcFldr: 0,
                swModified: 0,
                topFullScale: 10.0,
                type: 4,
                useBits: b'\x00',
                wModified: 1,
                waveNoteH: 0,
                whUnused: array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                whVersion: 1,
                whpad1: array([b'', b'', b'', b'\x02', b'', b''], dtype='|S1'),
                whpad2: 0,
                whpad3: 0,
                whpad4: 1,
            }
        }
    }
    .header {
        recordType -- igor object type (3 = wave)
        numDataBytes -- size in bytes
        version -- wavemetrics option
    }
    .data -- binary data

EXAMPLES:

    imem1 = a[1]['root'][b'imem1'].wave['wave']['wData']

    plot(numpy.frombuffer(a[1]['root'][b'imem1'].data, float64, 1001))

1. Create new WaveRecord class
"""

from igor import packed
import scipy

def folders(start,arr,temp,level=0):
    """
    Print nested dictionary names...
    :param start: first dict
    :param level: formatting indentation
    :return:
    """
    sep=":"
    for key in start.keys():
        if type(start.get(key))==dict:
            try:
                key.decode()
            except:
                #print(" "*4*level+key)
                temp.append(key)
                arr.append(sep.join(temp))
            else:
                #print(" "*4*level+key.decode())
                temp.append(key.decode())
                arr.append(sep.join(temp))
            #increase indentation
            folders(start.get(key),arr,temp,level+1)
            temp.pop(-1)

def checktype(item,typelist):
    assert type(typelist)==list
    print(item)

class pxp():
    pstruct = dict()
    def __init__(self,file):
        #include checking...
        self.pstruct=packed.load(file)

    def folders(self):
        #list folder tree starting at path...
        folderlist = []
        temp=[]
        folders(self.pstruct[1],arr=folderlist,temp=temp)
        folderlist.sort() #ensure consistency...
        return folderlist

    def folderinfo(self, path, types=("all")):
        """
        accept folder path and return tuple:
            - target path
            - item count
            - list of items
        :param path:
        :param type: vars, waves, folders, all
        :return:
        """
        assert type(types)==tuple
        loc = self.pstruct[1]
        for p in path.split(":"):
            try:
                loc[p]
            except:
                loc=loc[p.encode()]
            else:
                loc=loc[p]
        items = []
        for key in loc.keys():
            try:
                key.decode()
            except:
                items.append(key)
            else:
                items.append(key.decode())
        return (path,scipy.array(items).size,items)

    def getwave(self,path):
        """
        Takes full path to wave, separated by ":" and returns tuple of wave infomration...
        :param path: full path to wave, separated by ":"
        :return: (data array, deltax, data units, dimension units)
        """
        patharr = path.split(":")
        w = self.pstruct[1]['root']
        for name in patharr[1:]:
            w =  w[name.encode()]

        return (w.wave['wave']['wData'], w.wave['wave']['wave_header']['sfA'][0], w.wave['wave']['wave_header']['dataUnits'][0], w.wave['wave']['wave_header']['dimUnits'][0][0], path)

class wave():
    def __init__(self, intuple):
        self.data = intuple[0] #data
        self.deltax = intuple[1] #deltax
        self.dataunits = intuple[2] #dataunits
        self.dimunits = intuple[3] #dimunits
        self.name = intuple[4] #wave name
        self.csrA=0
        self.csrB=intuple[0].size

    def mean(self):
        return scipy.mean(self.data)
    def sum(self):
        return scipy.sum(self.data)
    def var(self):
        return sum([(point**2 - self.mean()**2) for point in self.data])/(self.npnts()-1)
    def sdev(self):
        return self.var() ** (1/2)
    def sem(self):
        return self.sdev()/((self.npnts())**(1/2))
    def rms(self):
        return (sum([point**2 for point in self.data])/self.npnts())**(1/2)
    def adev(self):
        pass
    def skew(self):
        pass
    def kurt(self):
        pass
    def min(self):
        return (int(scipy.where(self.data==self.data.min())[0]),self.data.min())
    def max(self):
        return (int(scipy.where(self.data==self.data.max())[0]),self.data.max())
    def npnts(self):
        return self.data.size
    def length(self):
        return self.npnts()*self.deltax

    def wavestats(self):
        print(self.name,"for %d to %d" % (self.csrA,self.csrB))
        print('   mean:', self.mean())
        print('    sum:', self.sum())
        print('    max:', self.max())
        print('    min:', self.min())
        print('  npnts:', self.npnts())
        print(' length:', self.length())
        print('    var:', self.var())
        print('   sdev:', self.sdev())
        print('    sem:', self.sem())
        print('    rms:', self.rms())
        print('   skew:', self.skew())
        print('   adev:', self.adev())
        print('   kurt:', self.kurt())
