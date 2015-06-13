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

    .version: ???,
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

1. Create new WaveRecord class
"""

import igor
from igor import record

a=record.WaveRecord()


class wave(igor.record.wave.WaveRecord):
    def __init__(self):