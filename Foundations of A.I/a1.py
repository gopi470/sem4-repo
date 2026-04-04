# Graph (DAG)
G = {
    'A': ['B', 'C'],
    'B': ['D', 'G'],
    'C': ['B', 'D'],
    'D': ['G'],
    'G': []
}

# --------------------------------------------------
# 1. Exhaustive Enumerate (PPT Algorithm)
# --------------------------------------------------
def exhaustive_enumerate(path):
    print(path)

    v = path[-1]

    for w in G[v]:
        exhaustive_enumerate(path + [w])


# --------------------------------------------------
# 2. Enumerate Search of Goal Node
# --------------------------------------------------
def enumerate_search(path):
    v = path[-1]

    if v == 'G':
        yield path[:]
    else:
        for w in G[v]:
            yield from enumerate_search(path + [w])


# --------------------------------------------------
# 3. Path Counts
# --------------------------------------------------
count = {node: 0 for node in G}

def count_paths(path):
    v = path[-1]

    count[v] += 1

    for w in G[v]:
        count_paths(path + [w])


# --------------------------------------------------
# DRIVER CODE
# --------------------------------------------------

print("DAG:", G, "\n")

# Exhaustive Enumeration
print("Exhaustive Enumeration of Paths:")
exhaustive_enumerate(['A'])


# Enumerate Goal Paths
print("\nEnumerate Search of the Goal Node:")
for p in enumerate_search(['A']):
    print(p)


# Path Counts
count_paths(['A'])

print("\nPath Counts:")
for k in count:
    print(k, ":", count[k])