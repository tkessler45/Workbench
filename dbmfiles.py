__author__ = 'tkessler'

import dbm
thedbmfile = dbm.open('dbmfile','c')
thedbmfile['first']="1"
thedbmfile['another']='Topher'
thedbmfile['help']='whhy?'

del thedbmfile['another']

print(len(thedbmfile))