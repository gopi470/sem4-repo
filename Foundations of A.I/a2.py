g = {
    'A': ['B', 'C'],
    'B': ['D', 'G'],
    'C': ['B', 'D'],
    'D': ['G'],
    'G': []
}

explored = set()
p = [None] * 7 


def depth_first_search(node):
    explored.add(node)

    if node == 'G':
        return True

    for neighbor in g[node]:
        if neighbor not in explored:
            p[ord(neighbor) - ord('A')] = node
            if depth_first_search(neighbor):
                return True

    return False


def print_path(node):
    #if node is not None:
        parent = p[ord(node) - ord('A')]
        if parent is not None:
            print_path(parent)
        print(node, end=" ")


def print_path_iter(node):
    stack = []

    while node is not None:
        stack.append(node)
        node = p[ord(node) - ord('A')]

    while stack:
        print(stack.pop(), end=" ")
    print()


# ---- Main Execution ----
print("DAG:", g)

if depth_first_search('A'):
    print("Parent Array:", p)
    print("Recursive Path to G:", end=" ")
    print_path('G')
    print("\nIterative Path to G:", end=" ")
    print_path_iter('G')
else:
    print("Node G not found.")
