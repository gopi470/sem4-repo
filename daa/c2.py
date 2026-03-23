n = 3
profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

max_profit = 0

def bound(i, curr_weight, curr_profit):
    if curr_weight >= capacity:
        return 0
    b = curr_profit
    w = curr_weight
    while i < n and w + weight[i] <= capacity:
        w += weight[i]
        b += profit[i]
        i += 1
    if i < n:
        b += (capacity - w) * (profit[i] / weight[i])
    return b

def knapsack(i, curr_weight, curr_profit):
    global max_profit

    if curr_weight <= capacity and curr_profit > max_profit:
        max_profit = curr_profit

    if i == n:
        return

    if bound(i, curr_weight, curr_profit) <= max_profit:
        return

    if curr_weight + weight[i] <= capacity:
        knapsack(i + 1, curr_weight + weight[i], curr_profit + profit[i])

    knapsack(i + 1, curr_weight, curr_profit)

knapsack(0, 0, 0)
print(max_profit)




