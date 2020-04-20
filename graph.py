import numpy as np
from collections import OrderedDict

class Vertex:
    def __init__(self, name):
        self.id = name
        self.adjacent = {}
        self.visited = 0

    def add_neighbor(self, v, weight):
        #if v in self.adjacent and self.adjacent[v] < weight:
        #    weight = self.adjacent[v]
        self.adjacent[v] = weight

    def weight(self, v):
        return self.adjacent[v]


class Edge:
    def __init__(self, id_, u, v, weight):
        self.id = id_
        self.u = u
        self.v = v
        self.weight = weight
        self.label = None

    def flatten(self):
        return self.u, self.v, self.weight


def next_edge_id(u, v):
    u, v = sorted([v, u])
    return int(0.5 * (u + v) * (u + v + 1) + v)


class Graph:

    def __init__(self, matrix=(), num_v=0):
        self.num_vertex = 0
        self.num_edges = 0
        self.vertex_map = OrderedDict()
        self.edges = OrderedDict()
        self.incident_edges = np.repeat({}, num_v)
        for (v, u, weight) in matrix:
            self.add_edge(v, u, weight)

    def add_vertex(self, node):
        if node not in self.vertex_map:
            self.num_vertex += 1
            self.vertex_map[node] = Vertex(node)
            self.incident_edges[node] = set()

    def opposite(self, e_id, node):
        e = self.edges[e_id]
        return e.v if node == e.u else e.u

    def add_edge(self, v, u, weight):
        self.num_edges += 1
        self.add_vertex(v)
        self.add_vertex(u)
        self.vertex_map[v].add_neighbor(u, weight)
        self.vertex_map[u].add_neighbor(v, weight)
        e_id = next_edge_id(u, v)
        self.edges[e_id] = Edge(e_id, u, v, weight)
        self.incident_edges[v].add(e_id)
        self.incident_edges[u].add(e_id)

    def adjacency_matrix(self):
        adj = np.zeros((self.num_vertex, self.num_vertex))
        for v in self.vertex_map:
            for u in self.vertex_map[v].adjacent:
                adj[v, u] += 1
        return adj

    def get_edges(self):  # O(m)
        return (e.flatten() for _, e in self.edges.items())

    def is_path(self, u, v):
        return is_path(self, u, v)

    def total_weight(self):
        return sum(e.weight for _, e in self.edges.items())


def load_file_matrix(path):
    with open(path) as f:
        graph = []
        num_vertex, _ = f.readline().split(' ')
        for row in f.readlines():
            v, u, w = map(int, row.rstrip('\n').split(' '))
            graph.append([v-1, u-1, w])
    return Graph(graph, num_vertex), int(num_vertex)


def load_files(paths):
    for path in paths:
        graph, num_vertex = load_file_matrix(path)
        yield path, graph, num_vertex


def tree_to_graph(t, G):  # O(|t|)
    mst = Graph((), G.num_vertex)
    for i, adj in enumerate(t):
        mst.add_vertex(i)
        if adj is not None:
            w = G.vertex_map[adj].weight(i)
            mst.add_edge(i, adj, w)
    return mst


def dfs(G: Graph, v):
    G.vertex_map[v].visited = 1
    for e in G.incident_edges[v]:
        if not G.edges[e].label:
            w = G.opposite(e, v)
            if G.vertex_map[w].visited == 0:
                G.edges[e].label = 'discovery_edge'
                dfs(G, w)
            else:
                G.edges[e].label = 'back_edge'


def dfs_clear(G: Graph, v):
    G.vertex_map[v].visited = 0
    for e in G.incident_edges[v]:
        if G.edges[e].label:
            w = G.opposite(e, v)
            if G.vertex_map[w].visited == 1:
                G.edges[e].label = None
                dfs_clear(G, w)
            else:
                G.edges[e].label = None


def is_path(G: Graph, s, t):
    dfs(G, s)
    cycle = G.vertex_map[t].visited
    dfs_clear(G, s)
    return cycle

