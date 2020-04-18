class UnionFind:
    es = {}

    def make_set(self, v):
        self.es[v] = Tree(v)
        self.es[v].p = self.es[v]
        self.es[v].rank = 0

    def find_set(self, v):
        if self.es[v] != self.es[v].p:
            self.es[v].p = self.find_set(self.es[v].p.value)
        return self.es[v].p

    def union(self, u, v):
        _link(self.find_set(u), self.find_set(v))


class Tree:
    def __init__(self, x):
        self.value = x
        self.p = self


def _link(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank = y.rank + 1



