# load inputs and compute things:
# weight and remove duplicates
_input = './test_inputs/input_random_32_800.txt'


def duplicates(_lines):
    copies = []
    adj = {}
    for line in _lines:
        line = line.rstrip('\n')
        u, v, w = line.split(' ')
        u, v, w = int(u), int(v), int(w)
        if u not in adj:
            adj[u] = {}
        if v in adj[u]:
            copies.append([u, v])
        else:
            adj[u][v] = w
        if v not in adj:
            adj[v] = {}
        if u not in adj[v]:
            adj[v][u] = w
    return copies


def selfloops(_lines):
    _loops = []
    for i, line in enumerate(_lines):
        u, v, w = line.strip('\n').split(' ')
        u, v, w = int(u), int(v), int(w)
        if u == v:
            _loops.append(i + 2)
    return _loops


with open(_input) as f:
    f.readline()
    lines = f.readlines()
    dup = duplicates(lines)
    loops = selfloops(lines)

print(f"copies:{dup}")
print(f"selfloops:{loops}")
