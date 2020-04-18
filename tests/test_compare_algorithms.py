from unittest import TestCase
from prim import prim
from graph import load_files
from kruskal_naive import kruskal
from kruskal_efficient import kruskal_opt
import os


inputs = []
outputs = []
input_dir = "../graphs"
for entry in os.scandir(input_dir):
    if entry.path.endswith('.txt') and entry.is_file():
        inputs.append(entry.path)


class TestCompareFast(TestCase):
    def test_kruskalopt_prim(self):
        mst_prim = []
        mst_kruskalopt = []
        for path, G, num_vertex in load_files(inputs[4:5]):
            pr = prim(G, 0)
            mst_prim.append(pr.total_weight())
        for path, G, num_vertex in load_files(inputs[4:5]):
            kr = kruskal_opt(G)
            mst_kruskalopt.append(kr.total_weight())
        assert all([w == oracle for w, oracle in zip(mst_prim, mst_kruskalopt)])

    def test_kruskal_prim(self):
        mst_prim = []
        mst_kruskal = []
        for path, G, num_vertex in load_files(inputs[4:5]):
            pr = prim(G, 0)
            mst_prim.append(pr.total_weight())
        for path, G, num_vertex in load_files(inputs[4:5]):
            kr = kruskal(G)
            mst_kruskal.append(kr.total_weight())
        assert all([w == oracle for w, oracle in zip(mst_prim, mst_kruskal)])


class TestCompareSlow(TestCase):
    def test_all(self):
        mst_prim = []
        mst_kruskal = []
        mst_kruskalopt = []
        for path, G, num_vertex in load_files(inputs[:30]):
            pr = prim(G, 0)
            kr = kruskal(G)
            kropt = kruskal_opt(G)
            mst_prim.append(pr.total_weight())
            mst_kruskal.append(kr.total_weight())
            mst_kruskalopt.append(kropt.total_weight())
        assert all([p == k and k == kopt for p, kopt, k in zip(mst_prim, mst_kruskalopt, mst_kruskal)])
