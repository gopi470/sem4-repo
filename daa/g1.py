import heapq
from collections import defaultdict

def prim_msf(n, edges):
    graph = defaultdict(list)

    # Build graph
    for u, v, w in edges:
        if u == v:
            continue
        graph[u].append((v, w))
        graph[v].append((u, w))

    visited = [False] * n
    forest = []

    # Process each component
    for start in range(n):
        if visited[start]:
            continue

        visited[start] = True
        heap = []

        for nei, wt in graph[start]:
            heapq.heappush(heap, (wt, start, nei))

        component_edges = []

        while heap:
            wt, u, v = heapq.heappop(heap)

            if visited[v]:
                continue

            visited[v] = True
            component_edges.append((u, v, wt))

            for nei, w2 in graph[v]:
                if not visited[nei]:
                    heapq.heappush(heap, (w2, v, nei))

        if component_edges:
            forest.append(component_edges)

    return forest


# -------- HARDCODED INPUT --------
n = 5
edges = [
    (0, 1, 2),
    (1, 2, 3),
    (3, 4, 1),
    (2, 3, 4)
]


# -------- PRINT INPUT --------
print("Input:")
print("Number of vertices:", n)
print("Edges (u, v, w):")
for e in edges:
    print(e)


# -------- PROCESS --------
msf = prim_msf(n, edges)


# -------- PRINT OUTPUT --------
print("\nOutput: Minimum Spanning Forest")

for i, component in enumerate(msf):
    print(f"\nTree {i+1}:")
    total_weight = 0
    for u, v, w in component:
        print(f"{u} -- {v} (weight = {w})")
        total_weight += w
    print("Total Weight:", total_weight)