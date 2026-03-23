class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add(self, val):
        self.items.append(val)

    def remove(self):
        val = self.items[0]
        del self.items[0]
        return val


# Version 1: Store (vertex, distance) in queue
def bfs_with_distance_in_queue(adj, start):
    verts = list(adj.keys())
    pos = {verts[i]: i for i in range(len(verts))}
    size = len(verts)

    visited = [False] * size
    level = [-1] * size

    q = Queue()
    q.add((start, 0))
    visited[pos[start]] = True

    while not q.is_empty():
        cur, depth = q.remove()
        level[pos[cur]] = depth

        for nbr in adj[cur]:
            if not visited[pos[nbr]]:
                visited[pos[nbr]] = True
                q.add((nbr, depth + 1))

    return {verts[i]: level[i] for i in range(size)}


# Version 2: Use distance array + visited
def bfs_with_distance_array(adj, start):
    verts = list(adj.keys())
    pos = {verts[i]: i for i in range(len(verts))}
    size = len(verts)

    visited = [False] * size
    level = [-1] * size

    q = Queue()
    q.add(start)
    visited[pos[start]] = True
    level[pos[start]] = 0

    while not q.is_empty():
        cur = q.remove()

        for nbr in adj[cur]:
            if not visited[pos[nbr]]:
                visited[pos[nbr]] = True
                level[pos[nbr]] = level[pos[cur]] + 1
                q.add(nbr)

    return {verts[i]: level[i] for i in range(size)}


# Version 3: Use distance array only (Best Version)
def bfs_using_distance_only(adj, start):
    verts = list(adj.keys())
    pos = {verts[i]: i for i in range(len(verts))}
    size = len(verts)

    level = [-1] * size

    q = Queue()
    q.add(start)
    level[pos[start]] = 0

    while not q.is_empty():
        cur = q.remove()

        for nbr in adj[cur]:
            if level[pos[nbr]] == -1:
                level[pos[nbr]] = level[pos[cur]] + 1
                q.add(nbr)

    return {verts[i]: level[i] for i in range(size)}



adj = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': []
}

start_vertex = 'A'

print("BFS Version 1:", bfs_with_distance_in_queue(adj, start_vertex))
print("BFS Version 2:", bfs_with_distance_array(adj, start_vertex))
print("BFS Version 3:", bfs_using_distance_only(adj, start_vertex))