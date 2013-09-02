from sys import stdin

funksjon = stdin.readline()
antall_noder = stdin.readline()
rot = int(stdin.readline())
ratatosk = int(stdin.readline())

if rot != ratatosk:
    noder = {}
    for linje in stdin.readlines():
        linje = linje.split()
        parent = linje.pop(0)
        for barn in linje:
            noder[int(barn)] = int(parent)
        
    dybde = 1
    current = noder[ratatosk]
    while current != rot:
        dybde += 1
        current = noder[current]
else:
    dybde = 0

print dybde