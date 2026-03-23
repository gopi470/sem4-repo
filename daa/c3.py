n = 3

duration = [2, 1, 2]
priority = [50, 40, 60]
deadline = [3, 2, 4]

best_priority = 0

def upper_bound(i, curr_priority):
    ub = curr_priority
    for j in range(i, n):
        ub += priority[j]
    return ub

def schedule(i, curr_time, curr_priority):
    global best_priority

    if curr_priority > best_priority:
        best_priority = curr_priority

    if i == n:
        return

    if upper_bound(i, curr_priority) <= best_priority:
        return

    if curr_time + duration[i] <= deadline[i]:
        schedule(i + 1,
                 curr_time + duration[i],
                 curr_priority + priority[i])

    schedule(i + 1, curr_time, curr_priority)

schedule(0, 0, 0)
print(best_priority)
