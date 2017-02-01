import sys
lista = []
c=0
linea=""
for i in open(sys.argv[1]):
    name = i.split()[3].split('i')[0].split('_')[0]
    c = lista.count(name)
    if c == 0:
        linea = " ".join(i.split()[:3]) + " " + name + " " +" ".join(i.split()[4:]).rstrip()
    else:
        linea = " ".join(i.split()[:3]) + " " + name + "_" + str(c+1) + " " +" ".join(i.split()[4:]).rstrip()
    print linea
    lista.append(name)
