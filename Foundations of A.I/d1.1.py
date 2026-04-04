# --------------------------------------------------
# Minimax with Alpha-Beta Pruning + Path (PPT Based)
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

def alpha_beta(n, alpha, beta, is_max):
    # if n is a leaf node then return evaluate(n), []
    if len(tree[n]) == 0:
        return values[n], []

    # if n is a MAX node
    if is_max:
        alpha_val = alpha
        best_path = []

        for c in tree[n]:
            val, path = alpha_beta(c, alpha_val, beta, False)

            if alpha_val < val:
                alpha_val = val
                best_path = [c] + path

            if beta <= alpha_val:
                return alpha_val, best_path   # PRUNE

        return alpha_val, best_path

    # else (MIN node)
    else:
        beta_val = beta
        best_path = []

        for c in tree[n]:
            val, path = alpha_beta(c, alpha, beta_val, True)

            if val < beta_val:
                beta_val = val
                best_path = [c] + path

            if beta_val <= alpha:
                return beta_val, best_path   # PRUNE

        return beta_val, best_path


# Run
value, path = alpha_beta('A', float('-inf'), float('inf'), True)

print("Optimal Value:", value)
print("Best Path:", ['A'] + path)