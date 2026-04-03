class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children else []

    def is_leaf(self):
        return len(self.children) == 0



n1 = Node(5)
n2 = Node(3)
n3 = Node(8)
n4 = Node(5)

left = Node(children=[n1, n2])
right = Node(children=[n3, n4])

root = Node(children=[left, right])



# Plain Minimax
minimax_count = 0

def minimax(node, maximizing):
    global minimax_count
    minimax_count += 1

    if node.is_leaf():
        return node.value

    if maximizing:
        return max(minimax(child, False) for child in node.children)
    else:
        return min(minimax(child, True) for child in node.children)



# Minimax with Trace
def minimax_trace(node, maximizing, depth=0):
    indent = "  " * depth

    if node.is_leaf():
        print(indent + "Leaf:", node.value)
        return node.value

    if maximizing:
        print(indent + "Max node")
        values = []
        for child in node.children:
            val = minimax_trace(child, False, depth + 1)
            values.append(val)
        result = max(values)
        print(indent + "Return:", result)
        return result
    else:
        print(indent + "Min node")
        values = []
        for child in node.children:
            val = minimax_trace(child, True, depth + 1)
            values.append(val)
        result = min(values)
        print(indent + "Return:", result)
        return result



# Minimax with Path
def minimax_with_path(node, maximizing):
    if node.is_leaf():
        return node.value, [node.value]

    if maximizing:
        best = float('-inf')
        best_path = []
        for child in node.children:
            val, path = minimax_with_path(child, False)
            if val > best:
                best = val
                best_path = path
        return best, best_path
    else:
        best = float('inf')
        best_path = []
        for child in node.children:
            val, path = minimax_with_path(child, True)
            if val < best:
                best = val
                best_path = path
        return best, best_path


# Alpha-Beta Pruning
alphabeta_count = 0

def alphabeta(node, alpha, beta, maximizing):
    global alphabeta_count
    alphabeta_count += 1

    if node.is_leaf():
        return node.value

    if maximizing:
        value = float('-inf')
        for child in node.children:
            value = max(value, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for child in node.children:
            value = min(value, alphabeta(child, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value




if __name__ == "__main__":

    print("Plain Minimax:")
    minimax_count = 0
    result = minimax(root, True)
    print("Result:", result)
    print("Nodes visited:", minimax_count)

    print("\nMinimax Trace:")
    minimax_trace(root, True)

    print("\nMinimax with Path:")
    score, path = minimax_with_path(root, True)
    print("Best Score:", score)
    print("Best Path:", path)

    print("\nAlpha-Beta Pruning:")
    alphabeta_count = 0
    result_ab = alphabeta(root, float('-inf'), float('inf'), True)
    print("Result:", result_ab)
    print("Nodes visited:", alphabeta_count)
