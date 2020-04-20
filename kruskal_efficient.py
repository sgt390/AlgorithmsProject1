import numpy as np
from graph import Graph, dfs
from copy import deepcopy
from kruskal_naive import order_edges
from unionfind import UnionFind


def kruskal_opt(G: Graph):
    G = deepcopy(G)
    mst = Graph((), G.num_vertex)
    uf = UnionFind()
    for v in G.vertex_map:  # O(n)
        mst.add_vertex(v)
        uf.make_set(v)
    edges = order_edges(G)  # O(log(n))
    for u, v, w in edges:  # O(m)
        if uf.find_set(u) != uf.find_set(v):
            mst.add_edge(u, v, w)
            uf.union(u, v)
    return mst
