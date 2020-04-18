import os
from graph import load_files
from prim import prim
from tqdm import tqdm
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pprint
from kruskal_naive import kruskal
from kruskal_efficient import kruskal_opt

directory = 'graphs'
pp = pprint.PrettyPrinter(indent=4)

paths = []
for entry in os.scandir(directory):
    if entry.path.endswith('.txt') and entry.is_file():
        paths.append(entry.path)


algorithms = {
    'Prim': prim,
    'Kruscal naive': kruskal,
    'Kruskal opt': kruskal_opt
}


def execute_mst(mst_algorithm):
    result = {
        'vertex': [],
        'time': [],
    }
    table = {}
    for path, G, num_vertex in tqdm(load_files(paths)):
        time0 = datetime.now()
        mst = mst_algorithm(G)
        time1 = datetime.now()
        result['time'].append(int((time1-time0).microseconds))
        result['vertex'].append(num_vertex)
        table[path] = mst.total_weight()
    return result, table


def mean_time(vs, ts):
    x_bar = []
    y_bar = []
    for vertex, time in zip(vs, ts):
        if vertex not in x_bar:
            y_bar.append(np.mean(sum((v for v in vs if v == vertex))))
            x_bar.append(vertex)
    return x_bar, y_bar


def plot_results(result, table):
    pp.pprint(table)


for i, alg in enumerate(algorithms):
    print(f'Algorithm: {alg}')
    result, table = execute_mst(algorithms[alg])
    plot_results(result, table)
