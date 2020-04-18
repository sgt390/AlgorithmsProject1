from unittest import TestCase
from prim import prim
from graph import load_files
from kruskal_naive import kruskal
from kruskal_efficient import kruskal_opt
import os


inputs = []
outputs = []
input_dir = "test_inputs"
output_dir = "test_outputs"
for entry in os.scandir(input_dir):
    if entry.path.endswith('.txt') and entry.is_file():
        inputs.append(entry.path)
for entry in os.scandir(output_dir):
    if entry.path.endswith('.txt') and entry.is_file():
        with open(entry.path) as f:
            o = int(f.readline().rstrip('\n'))
            outputs.append(o)


class TestOracle(TestCase):
    def test_prim(self):
        results = []
        for path, G, num_vertex in load_files(inputs):
            mst = prim(G, 0)
            results.append(mst.total_weight())
        assert all([w == oracle for w, oracle in zip(results, outputs)])

    def test_krusal(self):
        results = []
        for path, G, num_vertex in load_files(inputs):
            mst = kruskal(G)
            results.append(mst.total_weight())
        assert all([w == oracle for w, oracle in zip(results, outputs)])

    def test_kruskal_opt(self):
        results = []
        for path, G, num_vertex in load_files(inputs):
            mst = kruskal_opt(G)
            results.append(mst.total_weight())
        assert all([w == oracle for w, oracle in zip(results, outputs)])
