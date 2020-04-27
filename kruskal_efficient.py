from graph import Graph
from kruskal_naive import order_edges
from unionfind import UnionFind


def kruskal_opt(G: Graph):
    mst = Graph((), G.num_vertex)
    uf = UnionFind()
    for v in G.vertex_map:  # O(n)
        if v is not None:
            mst.add_vertex(v.id)
            uf.make_set(v.id)
    edges = order_edges(G)  # O(log(n))
    for u, v, w in edges:  # O(m)
        if uf.find_set(u) != uf.find_set(v):
            mst.add_edge(u, v, w)
            uf.union(u, v)
    return mst
