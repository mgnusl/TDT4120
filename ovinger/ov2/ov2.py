from sys import stdin

# var ikke definert i den gamle python-versjonen som 
# ligger paa noen av stud sine maskiner
True = 1
False = 0

class Node:
    barn = None 
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = 0

def dfs(rot):
    stack = [rot, 0]
    while stack:
        dybde = stack.pop()
        currentNode = stack.pop()
        if currentNode.ratatosk:
            return dybde
        while len(currentNode.barn) > 0:
            stack.append(currentNode.barn.pop())
            stack.append(dybde+1)
    

def bfs(r):
    queue = [r, 0]
    while len(queue) > 0:
        current = queue.pop(0)
        dybde = queue.pop(0)
        if current.ratatosk:
            return dybde
        for barn in current.barn:
            queue.append(barn)
            queue.append(dybde+1)

funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print bfs(start_node)