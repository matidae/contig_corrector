import sys
import collections

conteos = {i.strip().split()[0]:0 for i in open(sys.argv[1])}
for i in open(sys.argv[2]):
    name = i.strip().split()[1].split("_")[0]
    count = int(i.strip().split()[0])
    conteos[name] += count

od = collections.OrderedDict(sorted(conteos.items()))
for i in od:
    print i, od[i]
