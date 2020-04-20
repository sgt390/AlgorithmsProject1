from unittest import TestCase
from graph import Graph
from prim import prim
import numpy as np
from graph import load_file_matrix

G0 = Graph((
    (0, 1, 2),
    (1, 2, 30),
    (2, 3, 10),
    (2, 0, 50)
), 4)
Gn = Graph((
    (0, 1, 200),
    (1, 2, 2),
    (2, 3, 1),
    (2, 0, -10)
), 4)


class TestPrim(TestCase):
    def test_prim_tree(self):
        oracle = [[0., 1., 0., 0.],
                  [1., 0., 1., 0.],
                  [0., 1., 0., 1.],
                  [0., 0., 1., 0.]]
        mst = prim(G0, 0)
        assert np.array_equal(mst.adjacency_matrix(), oracle)

    def test_prim_w(self):
        oracle = 42
        mst = prim(G0, 0)
        w = mst.total_weight()
        assert w == oracle

    def test_input(self):
        path = "../graphs/input_random_01_10.txt"
        oracle = sum([4993, 1392, 8856, -433, 6590, -7462, 6658, -976, 9698])  # 9 edges
        Gi, _ = load_file_matrix(path)
        mst = prim(Gi, 0)
        w = mst.total_weight()
        assert w == oracle

    def test_negative(self):
        oracle = -7
        mst = prim(Gn, 0)
        w = mst.total_weight()
        assert w == oracle
