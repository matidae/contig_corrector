import sys

genecoor = []

with open(sys.argv[1]) as fh:
    for i in fh:
        namecoor = i.split()[2] + i.split()[3].split('_')[0] + i.split()[-1].strip()
        if namecoor not in genecoor:
            genecoor.append(namecoor)
            print i.strip()
        
