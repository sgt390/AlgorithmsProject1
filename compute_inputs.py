# load inputs and compute things:
# weight and remove duplicates
input = './test_inputs/input_random_32_800.txt'
#input = './test_inputs/input_random_1_10.txt'


def duplicates(lines):
    copies = []
    adj = {}
    for line in lines:
        line = line.rstrip('\n')
        u, v, w = line.split(' ')
        u, v, w = int(u), int(v), int(w)
        if not u in adj:
            adj[u] = {}
        if v in adj[u]:
            copies.append([u, v])
        else:
            adj[u][v] = w
        if not v in adj:
            adj[v] = {}
        if u not in adj[v]:
            adj[v][u] = w
    return copies


def selfloops(lines):
    loops = []
    for i, line in enumerate(lines):
        u, v, w = line.strip('\n').split(' ')
        u, v, w = int(u), int(v), int(w)
        if u == v:
            loops.append(i+2)
    return loops


with open(input) as f:
    f.readline()
    lines = f.readlines()
    dup = duplicates(lines)
    loops = selfloops(lines)


print(f"copies:{dup}")
print(f"selfloops:{loops}")


