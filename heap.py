import numpy as np


def min_heapify(A, i, node_id):  # O(log(|A|)
    lft = left(i)
    rgt = right(i)
    if lft < len(A) and A[lft][1] < A[i][1]:
        _min = lft
    else:
        _min = i
    if rgt < len(A) and A[rgt][1] < A[_min][1]:
        _min = rgt
    if _min != i:
        tmp = A[i]
        node_id[A[i][0]] = _min
        node_id[A[_min][0]] = i
        A[i] = A[_min]
        A[_min] = tmp
        min_heapify(A, _min, node_id)


def parent(i):
    return int(i/2)


def left(i):
    return 2*i


def right(i):
    return 2*i+1


def graph_to_min_heap(G, s):  # O(n)
    """
    :param G: Graph
    :param s: starting node
    :return: (array representing a min-heap, array that maps each node to its position in the min-heap array)
    """
    a = []
    node_id = list(range(G.num_vertex))
    for i, k in enumerate(G.vertex_map):  # O(n)
        if k is not None:
            v = k.id
            a.append((v, np.inf))
            node_id[v] = i
    a[node_id[s]] = (a[node_id[0]][0], s)
    build_min_heap(a, node_id)  # O(n) (a contains n elements)
    return a, node_id


def build_min_heap(A, node_id):  # O(n*log(n))
    """
    :param A: Array of tuples (node_id, weight) to be transformed to min_heap
    :param node_id: array that maps each node to its position in A
    :return: min-heap
    """
    for i in range(int(len(A)/2), -1, -1):
        min_heapify(A, i, node_id)


def heap_extract_min(A, node_id):  # O(log(|A|)
    """
    :param A: array organized as min-heap. Each element is (node_id, weight)
    :param node_id: array that maps each node to its position in A
    :return: node with the minimum weight
    """
    if len(A) < 1:
        raise KeyError
    _min = A[0]
    A[0] = A[len(A)-1]
    node_id[A[len(A) - 1][0]] = 0
    del A[len(A)-1]
    min_heapify(A, 0, node_id)  # O(log(|A|)
    return int(_min[0])


def heap_decrease_key(A, i, k, node_id):
    """
    :param A: array organized as min-heap. Each element is (node_id, weight)
    :param i: position of element in A to decrease
    :param k: decreasing value
    :param node_id: array that maps each node to its position in A
    :return: min-heap
    """
    if k > A[i][1]:
        raise KeyError
    A[i] = (A[i][0], k)
    while i > 0 and A[parent(i)][1] > A[i][1]:
        app = A[i]
        node_id[A[i][0]] = parent(i)
        node_id[A[parent(i)][0]] = i
        A[i] = A[parent(i)]
        A[parent(i)] = app
        i = parent(i)
