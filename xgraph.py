import networkx as nx
from networkx import minimum_spanning_tree as mst
from prim import prim
from graph import load_files
from kruskal_naive import kruskal

input = 'graphs/input_random_05_20.txt'

edges = []
with open(input) as f:
    f.readline()
    for x in f.readlines():
        v, u, w = x.rstrip('\n').split(' ')
        edges.append([int(v), int(u), int(w)])

G = nx.Graph()
G.add_weighted_edges_from(edges)
T: nx.Graph = mst(G)

wnetworkx = 0
for v, u in T.edges:
    w = T.adj[v][u]['weight']
    wnetworkx += w

for path, G, num_vertex in load_files([input]):
    mst = prim(G, 0)
wprim = mst.total_weight()

for path, G, num_vertex in load_files([input]):
    mst = kruskal(G)
wkruskal = mst.total_weight()

print(f"prim: {wprim}\nkruskal: {wkruskal}\nxnetworx: {wnetworkx}")
