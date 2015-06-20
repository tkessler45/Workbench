__author__ = 'tkessler'

# walk each folder in the python system path
# skip visited paths
# collect files of specific type...

import sys, os

visited = []
files = []
for path in sys.path:
    for (dirpath, dirnames, filenames) in os.walk(path):
        if dirpath in visited:
            continue
        else:
            visited.append(dirpath)
            for file in filenames:
                if file.endswith(".py"):
                    files.append((os.path.getsize(os.path.join(dirpath,file)),os.path.join(dirpath,file)))

files.sort(reverse=True)
for tpl in files[:2]:
    print(tpl)