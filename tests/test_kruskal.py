from unittest import TestCase
from graph import Graph
from kruskal_naive import kruskal
import numpy as np


class TestKruskal(TestCase):
    def test_kruskal_tree(self):
        G0 = Graph((
            (0, 1, 2),
            (1, 2, 30),
            (2, 3, 10),
            (2, 0, 50)
        ), 4)
        oracle = [[0., 1., 0., 0.],
                  [1., 0., 1., 0.],
                  [0., 1., 0., 1.],
                  [0., 0., 1., 0.]]
        mst = kruskal(G0)
        assert np.array_equal(mst.adjacency_matrix(), oracle)

    def test_kruskal_w(self):
        G0 = Graph((
            (0, 1, 2),
            (1, 2, 30),
            (2, 3, 10),
            (2, 0, 50)
        ), 4)
        mst = kruskal(G0)
        w = mst.total_weight()
        assert 42 == w

