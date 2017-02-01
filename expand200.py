import sys

for i in open(sys.argv[1]):
    desc = " ".join(i.split()[:6])
    cooraux = i.split()[6].split(',')
    coor = ",".join([i for i in cooraux if ':' in i])
    csta = int(coor.split(':')[0]) - 200
    cmid = ":".join(coor.split(':')[1:-1])
    cend = int(coor.split(':')[-1]) + 200
    if csta < 1 :
        csta = 1
    line = desc + " " + ":".join(map(str,[csta, cmid, cend]))
    line = line.replace('::',':')
    print line
