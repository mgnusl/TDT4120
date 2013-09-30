from sys import stdin

Inf = float(1e3000)
False = 0
True = 1

def mst(nm):
    tree = prims(nm)
    sum = 0
    for (fra, til) in tree:
        sum = max(sum, nm[fra][til])
    return sum

def prims(nm):
    n = len(nm)
    tree = []
    lowest_cost = [Inf] * n
    best_neighbor = [None] * n
    not_found = range(1, n)
    previous = 0
    while len(not_found) > 0:
        for i in not_found:
            if nm[i][previous] < lowest_cost[i]:
                best_neighbor[i] = previous
                lowest_cost[i] = nm[i][previous]
        mincost = Inf
        for i in not_found:
            if lowest_cost[i] < mincost:
                nextF = i
                nextT = best_neighbor[i]
                mincost = lowest_cost[i]
        tree.append( (nextF,nextT) )
        not_found.remove(nextF)
        previous = nextF
    return tree


linjer = []
for str in stdin:
    linjer.append(str)
n = len(linjer)
nabomatrise = [None] * n
node = 0
for linje in linjer:
    nabomatrise[node] = [Inf] * n
    for k in linje.split():
        data = k.split(':')
        nabo = int(data[0])
        vekt = int(data[1])
        nabomatrise[node][nabo] = vekt
    node += 1
print mst(nabomatrise)