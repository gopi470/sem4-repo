class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        self.parent[pu] = pv
        return True


def kruskal_msf(n, edges):
    dsu = DSU(n)
    filtered_edges = []

    # Filter edges (remove self-loops)
    for u, v, w in edges:
        if u != v:
            a, b = min(u, v), max(u, v)
            filtered_edges.append((w, a, b, u, v))

    # Sort edges by weight
    filtered_edges.sort()

    mst = []
    total_weight = 0

    # Kruskal's algorithm
    for w, a, b, u, v in filtered_edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


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
mst, total_weight = kruskal_msf(n, edges)


# -------- PRINT OUTPUT --------
print("\nOutput: Minimum Spanning Forest (Kruskal)")

print("\nEdges in MSF:")
for u, v, w in mst:
    print(f"{u} -- {v} (weight = {w})")

print("\nTotal Weight:", total_weight)