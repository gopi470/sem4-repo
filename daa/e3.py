from collections import deque


def bfs(residual, s, t, parent):
    visited = [False] * len(residual)
    queue = deque([s])
    visited[s] = True

    while queue:
        u = queue.popleft()

        for v in range(len(residual)):
            if not visited[v] and residual[u][v] > 0:
                parent[v] = u
                visited[v] = True
                queue.append(v)

    return visited[t]



def ford_fulkerson(graph, source, sink):
    residual = [row[:] for row in graph]   # Copy graph
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(residual, source, sink, parent):
        path_flow = float("inf")
        v = sink

        # Find minimum capacity in augmenting path
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual[u][v])
            v = u

        max_flow += path_flow

        # Update residual capacities
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = u

    return max_flow




# Graph adjacency matrix
graph = [
    [0, 10, 5, 0],   # S
    [0, 0, 15, 10],  # A
    [0, 0, 0, 10],   # B
    [0, 0, 0, 0]     # T
]

source = 0
sink = 3

max_flow = ford_fulkerson(graph, source, sink)
print("Maximum Flow =", max_flow)
