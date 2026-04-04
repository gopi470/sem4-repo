from collections import deque

# --------------------------------------------------
# Breadth First Search (PPT Algorithm)
# --------------------------------------------------
def bfs(adj, start, goal=None):
    # d[v] ← ∞
    d = {v: float('inf') for v in adj}

    # parent[v] ← None
    parent = {v: None for v in adj}

    # Queue
    q = deque()

    # d[s] ← 0
    d[start] = 0

    # add (-, s)
    q.append((None, start))

    # while Queue is not empty
    while q:
        u, v = q.popleft()

        # if goal(v) then stop (optional PPT extension)
        if v == goal:
            break

        # foreach successor w of v
        for w in adj[v]:
            if d[w] == float('inf'):
                d[w] = d[v] + 1
                parent[w] = v
                q.append((v, w))

    return d, parent


# --------------------------------------------------
# Path Reconstruction
# --------------------------------------------------
def get_path(parent, target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    path.reverse()
    return path


# --------------------------------------------------
# GRAPH
# --------------------------------------------------
adj = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': []
}

start_vertex = 'A'
goal = 'E'


# --------------------------------------------------
# DRIVER
# --------------------------------------------------
print("Graph:", adj)

distance, parent = bfs(adj, start_vertex, goal)

print("\nDistance (d[v]):")
for k in distance:
    print(k, ":", distance[k])

# --------------------------------------------------

print("\nParent:")
for k in parent:
    print(k, ":", parent[k])

# --------------------------------------------------

print("\nPaths from", start_vertex)
for node in adj:
    if distance[node] != float('inf'):
        print(node, ":", get_path(parent, node))

# --------------------------------------------------

print(f"\nShortest path from {start_vertex} to {goal}:")
if distance[goal] != float('inf'):
    print(" -> ".join(get_path(parent, goal)))
else:
    print("No path found")