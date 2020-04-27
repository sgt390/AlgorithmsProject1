import os
from graph import load_files
from prim import prim
from tqdm import tqdm
import time
import matplotlib.pyplot as plt
import numpy as np
from pprint import PrettyPrinter
from kruskal_naive import kruskal
from kruskal_efficient import kruskal_opt

directory = 'graphs'
pprint = PrettyPrinter(indent=4).pprint

paths = []
for entry in os.scandir(directory):
    if entry.path.endswith('.txt') and entry.is_file():
        paths.append(entry.path)

algorithms = {
    'Prim': prim,
    'Kruskal opt': kruskal_opt,
    'Kruskal naive': kruskal
}


def execute_mst(mst_algorithm):
    times = []
    nodes = []
    results = {}
    for path, G, num_vertex in tqdm(load_files(paths)):
        if mst_algorithm == 'Kruskal naive' and num_vertex > 40000:
            break
        start = time.perf_counter()
        mst = mst_algorithm(G)
        end = time.perf_counter()
        times.append(end - start)
        nodes.append(num_vertex)
        results[path] = mst.total_weight()
    return (nodes, times), results


def mean_time(vs, ts):
    x_bar = []
    y_bar = []
    for vertex, _time in zip(vs, ts):
        if vertex not in x_bar:
            y_bar.append(np.mean(sum((v for v in vs if v == vertex))))
            x_bar.append(vertex)
    return x_bar, y_bar


def plot_times(results, algorithm, pos):
    nodes, times = results
    plt.subplot(310 + pos)
    plt.xlabel('# Nodes')
    plt.ylabel('Time')
    plt.plot(nodes, times, label=algorithm)


for i, alg in enumerate(algorithms):
    result, table = execute_mst(algorithms[alg])
    print(f'Algorithm: {alg}')
    pprint(table)
    plot_times(result, alg, i + 1)
plt.show()
