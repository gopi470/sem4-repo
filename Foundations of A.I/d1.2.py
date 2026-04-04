# --------------------------------------------------
# Minimax (Without Alpha-Beta) + Path (PPT Based)
# --------------------------------------------------

# Example tree (adjacency list)
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Terminal node values
values = {
    'D': 3,
    'E': 5,
    'F': 6,
    'G': 9
}

def minimax(n, is_max):
    # if n is a leaf node then return evaluate(n), []
    if len(tree[n]) == 0:
        return values[n], []

    # if n is a MAX node
    if is_max:
        max_val = float('-inf')
        best_path = []

        for c in tree[n]:
            val, path = minimax(c, False)

            if max_val < val:
                max_val = val
                best_path = [c] + path

        return max_val, best_path

    # else (MIN node)
    else:
        min_val = float('inf')
        best_path = []

        for c in tree[n]:
            val, path = minimax(c, True)

            if val < min_val:
                min_val = val
                best_path = [c] + path

        return min_val, best_path


# Run
value, path = minimax('A', True)

print("Optimal Value:", value)
print("Best Path:", ['A'] + path)