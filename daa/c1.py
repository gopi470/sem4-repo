import sys

INF = sys.maxsize
n = 4

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

visited = [False] * n
best_cost = INF


def lower_bound():
    lb = 0
    for i in range(n):
        if not visited[i]:
            lb += min(cost[i])
    return lb

def branch_and_bound(curr_pos, count, curr_cost):
    global best_cost
    if count == n:
        if cost[curr_pos][0] != INF:
            best_cost = min(best_cost, curr_cost + cost[curr_pos][0])
        return
    if curr_cost + lower_bound() >= best_cost:
        return
    for i in range(n):
        if not visited[i] and cost[curr_pos][i] != INF:
            visited[i] = True
            branch_and_bound(i, count + 1, curr_cost + cost[curr_pos][i])
            visited[i] = False

visited[0] = True
branch_and_bound(0, 1, 0)

print(best_cost)

