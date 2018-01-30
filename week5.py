import math
INFINITY = math.inf # float("inf")

class myqueue(list):
 def __init__(self,a=[]):
 list.__init__(self,a)

 def dequeue(self):
 return self.pop(0)

 def enqueue(self,x):
 self.append(x)

class Vertex:
 def __init__(self, data):
 self.data = data

 def __repr__(self): # voor afdrukken
 return str(self.data)

 def __lt__(self, other): # voor sorteren
 return self.data < other.data

def vertices(G):
 return sorted(G)

def edges(G):
 return [(u,v) for u in vertices(G) for v in G[u]]

def clear(G):
 for v in vertices(G):
 k = [e for e in vars(v) if e != 'data']
 for e in k:
 delattr(v,e)

def BFS(G,s):
 V = vertices(G)
 s.predecessor = None
 s.distance = 0
 for v in V:
 if v != s:
 v.distance = INFINITY
 q = myqueue()
 q.enqueue(s)
 while q:
 u = q.dequeue()
 for v in G[u]:
 if v.distance == INFINITY:
 v.distance = u.distance + 1
 v.predecessor = u
 q.enqueue(v)

def show_tree_info(G):
 print('tree:', end = ' ')
 for v in vertices(G):
 print('(' + str(v), end = '')
 if hasattr(v,'distance'):
 print(',d:' + str(v.distance), end = '')
 if hasattr(v,'predecessor'):
 print(',p:' + str(v.predecessor), end = '')
 print(')', end = ' ')
 print()

def show_sorted_tree_info(G):
 print('sorted tree:')
 V = vertices(G)
 V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
 V.sort(key = lambda x: (x.distance,x.predecessor))
 d = 0
 for v in V:
 if v.distance > d:
 print()
 d += 1
 print('(' + str(v) + ',d:' + str(v.distance) + ',p:'
 + str(v.predecessor), end = '')
 print(')', end = ' ')
 print()

def path_BFS(G,u,v):
 BFS(G,u)
 a = []
 if hasattr(v,'predecessor'):
 current = v
 while current:
 a.append(current)
 current = current.predecessor
 a.reverse()
 return a

def is_connected(G):
 BFS(G, vertices(G)[0])

 for vertex in G:
 if vertex.distance == INFINITY:
 return False
 return True

def no_cycles(G):
 s = vertices(G)[0]
 V = vertices(G)

 s.predecessor = None
 s.distance = 0

 for vertex in V:
 if vertex != s:
 vertex.distance = INFINITY
 q = myqueue()
 q.enqueue(s)

 while q:
 u = q.dequeue()
 for vertex in G[u]:
 if vertex.distance == INFINITY:
 vertex.distance = u.distance + 1
 vertex.predecessor = u
 q.enqueue(vertex)
 elif u.predecessor != vertex:
 return False
 return True

def get_bridges(G):
 bridges = []

 for e in edges(G):
 # verwijder de brug
 G[e[0]].remove(e[1])
 G[e[1]].remove(e[0])
 # kijk of er nog eenv verbinding is
 if not is_connected(G):
 bridges.append(e)
 # zet ze er weer in
 G[e[0]].append(e[1])
 G[e[1]].append(e[0])

 return bridges

def is_stongly_connected(G):
 if not is_connected(G):
 return False
 other = {}
 for edge in edges(G):
 if edge[1] in other.keys():
 other[edge[1]].append(edge[0])
 else:
 other[edge[1]] = [edge[0]]

 return is_connected(other)

def node_in_cycle(G, s):
 V = vertices(G)
 s.distance = 0
 # zet alles naar oneindig behalve s
 for v in V:
 if v != s:
 v.distance = INFINITY
 q = myqueue()
 q.enqueue(s)
 while q:
 u = q.dequeue()
 for v in G[u]:
 if v == s:
 return True
 if v.distance == INFINITY:
 v.distance = u.distance + 1
 q.enqueue(v)
 return False

def is_euler_graph(G):
 for vertex in G:
 if len(G[vertex]) & 1:
 return False
 return True

def get_euler_circuit(G, s):
 if not is_euler_graph(G):
 return []

 path = [s]
 while G[s]:
 tmp = None

 for t in G[s]:
 tmp = t
 if (s, t) not in get_bridges(G):
 break

 if tmp is not None:
 path.append(tmp)
 G[s].remove(tmp)
 G[tmp].remove(s)
 s = tmp

 return path

v2 = [Vertex(i) for i in range(5)]

G5 = {v2[0]:[v2[1]],
 v2[1]:[v2[2]],
 v2[2]:[v2[3],v2[4]],
 v2[3]:[],
 v2[4]:[v2[1]]}

for v in vertices(G5):
 print(node_in_cycle(G5,v))

v = [Vertex(i) for i in range(8)]

G = {v[0]:[v[1],v[4]],
 v[1]:[v[0],v[5]],
 v[2]:[v[3],v[5],v[6]],
 v[3]:[v[2],v[6],v[7]],
 v[4]:[v[0]],
 v[5]:[v[1],v[2],v[6]],
 v[6]:[v[2],v[3],v[5],v[7]],
 v[7]:[v[3],v[6]]}

G1 = {
 v[0]: [v[4], v[5]],
 v[1]: [v[4], v[5], v[6]],
 v[2]: [v[4], v[5], v[6]],
 v[3]: [v[7]],
 v[4]: [v[0], v[1], v[5]],
 v[5]: [v[1], v[2], v[4]],
 v[6]: [v[1], v[2]],
 v[7]: [v[3]]
}

G2 = {
 v[0]: [v[4], v[5]],
 v[1]: [v[4], v[5], v[6]],
 v[2]: [v[4], v[5], v[6]],
 v[4]: [v[0], v[1], v[5]],
 v[5]: [v[1], v[2], v[4]],
 v[6]: [v[1], v[2]],
}

G3 = {
 v[0]: [v[4], v[5]],
 v[1]: [v[4], v[6]],
 v[2]: [v[5]],
 v[3]: [v[7]],
 v[4]: [v[0], v[1]],
 v[5]: [v[0], v[2]],
 v[6]: [v[1]],
 v[7]: [v[3]],
}

G4 = {
 v[0]: [v[1], v[3]],
 v[1]: [v[0], v[2]],
 v[2]: [v[1], v[3], v[4]],
 v[3]: [v[0], v[2]],
 v[4]: [v[2], v[5], v[6]],
 v[5]: [v[4], v[6]],
 v[6]: [v[4], v[5], v[7]],
 v[7]: [v[6]],
}

G5 = {
 v[0]: [v[1]],
 v[1]: [v[2]],
 v[2]: [v[0]],
}

G6 = {
 v[0]: [v[1]],
 v[2]: [v[0], v[1]],
}

G7 = {
 v[0]: [v[1], v[2]],
 v[1]: [v[2], v[0]],
 v[2]: [v[0], v[1]],
}

G8 = {
 v[0]: [v[1], v[2]],
 v[1]: [v[0], v[3]],
 v[2]: [v[0], v[3]],
 v[3]: [v[1], v[2], v[4], v[6]],
 v[4]: [v[3], v[5], v[6], v[7]],
 v[5]: [v[4], v[6]],
 v[6]: [v[3], v[4], v[5], v[7]],
 v[7]: [v[4], v[6]],
}

print("vertices(G):",vertices(G))
print("edges(G):",edges(G))

print("is_connected(G1):", is_connected(G1))
print("is_connected(G2):", is_connected(G2))

print("no_cycles(G1):", no_cycles(G1))
print("no_cycles(G2):", no_cycles(G2))
print("no_cycles(G3):", no_cycles(G3))

print("get_bridges(G4):", get_bridges(G4))

print("path_BFS(G,v[1],v[7]):",path_BFS(G,v[1],v[7]))
print("strongly_connected(G5):", is_stongly_connected(G5))
print("strongly_connected(G6):", is_stongly_connected(G6))
print("is_euler_graph(G8):", is_euler_graph(G8))

for vertex in vertices(G8):
 print("get_euler_circuit(G8, {}):".format(vertex), get_euler_circuit(G8, vertex))
