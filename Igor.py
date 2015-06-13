__author__ = 'tkessler'

from igor import packed

a = packed.load('/Users/tkessler/igortest.pxp')

rawwaves = a[0]
datastructure = dict(a[1])
rootstructure = datastructure['root']
awave = rootstructure.get('imem31'.encode())

#a = igor.record.wave.WaveRecord

print(awave.wave['version'])