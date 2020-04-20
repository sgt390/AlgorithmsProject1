import numpy as np
from graph import Graph, dfs
from copy import deepcopy


def kruskal(G: Graph):
    mst = Graph((), G.num_vertex)
    for v in G.vertex_map:  # O(n)
        mst.add_vertex(v)
    edges = order_edges(G)  # O(n*log(n))
    for u, v, w in edges:  # O(m)
        if not mst.is_path(u, v):  # O(n+m)
            mst.add_edge(u, v, w)
        if mst.num_edges == mst.num_vertex - 1:
            break
    return mst


def order_edges(G): # O(m*log(m))
    edges = G.get_edges()
    dtype = [('u', int), ('v', int), ('weight', int)]
    edges = np.array(list(edges), dtype)
    edges = np.sort(edges, kind='mergesort', order='weight')
    return edges
