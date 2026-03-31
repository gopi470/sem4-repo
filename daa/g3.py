import heapq
from collections import defaultdict

def dijkstra(n, edges, source):
    graph = defaultdict(list)

    # Build graph
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [float('inf')] * n
    parent = [-1] * n

    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    return dist, parent


# -------- HARDCODED INPUT --------
n = 5
edges = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 4, 3),
    (3, 4, 1)
]
source = 0


# -------- PRINT INPUT --------
print("Input:")
print("Number of vertices:", n)
print("Edges (u, v, w):")
for e in edges:
    print(e)
print("Source:", source)


# -------- PROCESS --------
dist, parent = dijkstra(n, edges, source)


# -------- FUNCTION TO PRINT PATH --------
def print_path(parent, v):
    path = []
    while v != -1:
        path.append(v)
        v = parent[v]
    return path[::-1]


# -------- PRINT OUTPUT --------
print("\nOutput: Shortest Paths (Dijkstra)\n")

for i in range(n):
    print(f"Vertex {i}:")
    print("Distance =", dist[i])
    print("Path =", print_path(parent, i))
    print()