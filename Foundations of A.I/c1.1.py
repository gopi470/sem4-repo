import heapq

# --------------------------------------------------
# GRAPH (Adjacency list with weights)
# Each node maps to list of (neighbor, cost)
# --------------------------------------------------
G = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('G', 5)],
    'C': [('D', 1)],
    'D': [('G', 1)],
    'G': []
}

# --------------------------------------------------
# HEURISTIC VALUES h(n)
# Estimated cost from node → goal
# Used in Greedy & A* search
# --------------------------------------------------
h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'G': 0
}

# --------------------------------------------------
# GENERIC PRIORITY SEARCH
# mode = "ucs" | "greedy" | "astar"
# --------------------------------------------------
def search(start, goal, mode):

    pq = []  # priority queue (min-heap)
    heapq.heappush(pq, (0, start))  # (priority, node)

    parent = {start: None}  # to reconstruct path

    # cost[v] = g(n) → actual cost from start to v
    cost = {node: float('inf') for node in G}
    cost[start] = 0

    # --------------------------------------------------
    # MAIN LOOP
    # --------------------------------------------------
    while pq:
        _, v = heapq.heappop(pq)  # get node with lowest priority

        # If goal reached → reconstruct path
        if v == goal:
            path = []
            while v:
                path.append(v)
                v = parent[v]
            return path[::-1]   # reverse path

        # Explore neighbors
        for w, wt in G[v]:
            g = cost[v] + wt   # new cost to reach neighbor

            # --------------------------------------------------
            # SELECT PRIORITY BASED ON MODE
            # --------------------------------------------------

            if mode == "ucs":
                # Uniform Cost Search
                # Priority = actual cost so far
                priority = g

            elif mode == "greedy":
                # Greedy Best First Search
                # Priority = heuristic only (ignore path cost)
                priority = h[w]

            elif mode == "astar":
                # A* Search
                # Priority = actual cost + heuristic
                priority = g + h[w]

            else:
               return "Mode Error"

            # --------------------------------------------------

            # Relaxation step (update if better path found)
            if g < cost[w]:
                cost[w] = g
                parent[w] = v
                heapq.heappush(pq, (priority, w))

    return "No Path"


# --------------------------------------------------
# RUN ALL SEARCH STRATEGIES
# --------------------------------------------------
print("UCS       :", search('A', 'G', "ucs"))
print("Greedy    :", search('A', 'G', "greedy"))
print("A*        :", search('A', 'G', "astar"))