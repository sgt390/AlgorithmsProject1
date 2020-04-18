import numpy as np
from graph import Graph, tree_to_graph
from heap import graph_to_min_heap, heap_extract_min, heap_decrease_key


def prim(G: Graph, s=0):
    """
    :param G: Graph
    :param s: starting node (index)
    :return: Minimum spanning tree (graph), sum of weights
    """
    parent = np.repeat(None, G.num_vertex)  # Parent of each Node in the mst
    Q, node_id = graph_to_min_heap(G, s)  # O(n)
    # "node_in_Q" and "node_id" save information about the array Q (if a node is present, and the node index in Q).
    # In both cases, the time spent searching is reduced from O(n) to O(1).
    node_in_Q = np.repeat(True, G.num_vertex)
    # while cycle total: O(n*log(n))
    while len(Q):  # O(n)
        u = heap_extract_min(Q, node_id)  # O(log(n))
        node_in_Q[u] = False
        for v in G.vertex_map[u].adjacent:  # total of O(m) (also considering the outer cycle)
            if node_in_Q[v] and G.vertex_map[u].weight(v) < Q[node_id[v]][1]:
                parent[v] = u
                k = G.vertex_map[u].weight(v)
                heap_decrease_key(Q, node_id[v], k, node_id)  # O(log(n))
    return tree_to_graph(parent, G)

