# Graph (DAG)
G = {
    'A': ['B', 'C'],
    'B': ['D', 'G'],
    'C': ['B', 'D'],
    'D': ['G'],
    'G': []
}

# explored set and parent array
explored = set()
parent = {node: None for node in G}


# --------------------------------------------------
# Depth First Search (PPT Algorithm)
# --------------------------------------------------
def depth_first_search(v):
    # if v is a goal vertex then return
    if v == 'G':
        return

    # if not explored[v]
    if v not in explored:
        explored.add(v)

        # foreach vw ∈ E do
        for w in G[v]:
            parent[w] = v
            depth_first_search(w)


# --------------------------------------------------
# Depth First Search To Goal
# --------------------------------------------------
def depth_first_search_goal(v, goal):
    # if v is a goal vertex then return True
    if v == goal:
        return True

    # if not explored[v]
    if v not in explored:
        explored.add(v)

        # foreach vw ∈ E do
        for w in G[v]:
            parent[w] = v
            if depth_first_search_goal(w, goal):
                return True   # stop when goal found

    return False

# --------------------------------------------------
# Print Path (Recursive)
# --------------------------------------------------
def print_path(v):
    if parent[v] is not None:
        print_path(parent[v])
    print(v, end=" ")


# --------------------------------------------------
# Print Path (Iterative)
# --------------------------------------------------
def print_path_iter(v):
    stack = []
    while v is not None:
        stack.append(v)
        v = parent[v]

    while stack:
        print(stack.pop(), end=" ")
    print()

# --------------------------------------------------

def get_path_goal(target):
    path = []
    while target is not None:
        path.append(target)
        target = parent[target]
    path.reverse()
    return path


# --------------------------------------------------
# DRIVER
# --------------------------------------------------
print("DAG:", G)

depth_first_search('A')

print("Parent:", parent)

print("Recursive Path to G:", end=" ")
print_path('G')

print("\nIterative Path to G:", end=" ")
print_path_iter('G')


start = 'A'
goal = 'G'
found = depth_first_search_goal(start, goal)


if found:
    print("Path from", start, "to", goal, ":")
    print(" -> ".join(get_path_goal(parent)))
else:
    print("No path found")