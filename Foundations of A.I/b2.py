class Queue:
    def __init__(self):
        self.box = []

    def is_empty(self):
        return len(self.box) == 0

    def add(self, val):
        self.box.append(val)

    def remove(self):
        item = self.box[0]
        del self.box[0]
        return item


def breadth_first_search(adjlist, start):
    verts = list(adjlist.keys())
    pos = {verts[k]: k for k in range(len(verts))}
    n = len(verts)

    dist = [-1] * n
    parent = [-1] * n

    q = Queue()
    q.add(start)
    dist[pos[start]] = 0

    while q.is_empty() == False:
        cur = q.remove()
        for nxt in adjlist[cur]:
            if dist[pos[nxt]] == -1:
                parent[pos[nxt]] = pos[cur]
                dist[pos[nxt]] = dist[pos[cur]] + 1
                q.add(nxt)

    return parent, dist, verts


def print_path(node_idx, parent, verts):
    if node_idx == -1:
        return
    print_path(parent[node_idx], parent, verts)
    print(verts[node_idx], end=" ")


def bfs_goal(adjlist, start, goal):
    parent, dist, verts = breadth_first_search(adjlist, start)
    pos = {verts[k]: k for k in range(len(verts))}

    if dist[pos[goal]] == -1:
        print("No path")
    else:
        print_path(pos[goal], parent, verts)
        print()
        print(dist[pos[goal]])


def bfs_goal_yield(adjlist, start, goal):
    verts = list(adjlist.keys())
    pos = {verts[k]: k for k in range(len(verts))}
    n = len(verts)

    dist = [-1] * n
    parent = [-1] * n

    q = Queue()
    q.add(start)
    dist[pos[start]] = 0

    while q.is_empty() == False:
        cur = q.remove()
        if cur == goal:
            return parent, dist, verts

        for nxt in adjlist[cur]:
            if dist[pos[nxt]] == -1:
                parent[pos[nxt]] = pos[cur]
                dist[pos[nxt]] = dist[pos[cur]] + 1
                q.add(nxt)

    return parent, dist, verts


adjlist = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': [],
    'F': []
}

startvertex = 'A'
goalvertex = 'F'

print("BFS parent and distance:")
p, d, v = breadth_first_search(adjlist, startvertex)
print(p)
print(d)

print("BFS path and distance to goal:")
bfs_goal(adjlist, startvertex, goalvertex)

print("BFS goal yield result:")
p2, d2, v2 = bfs_goal_yield(adjlist, startvertex, goalvertex)
print(p2)
print(d2)
