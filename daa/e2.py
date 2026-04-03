# Function bpm(u, graph, seen, matchR)
def bpm(u, graph, seen, matchR):
    for v in graph[u]:
        if not seen[v]:
            seen[v] = True

            # If job is not matched OR previously matched applicant
            # can get another job
            if matchR[v] == -1 or bpm(matchR[v], graph, seen, matchR):
                matchR[v] = u
                return True
    return False


# Function max_bipartite_matching(graph, m, n)
def max_bipartite_matching(graph, m, n):
    matchR = [-1] * m   # Jobs matched to applicants
    result = 0

    for u in range(n):  # For each applicant
        seen = [False] * m
        if bpm(u, graph, seen, matchR):
            result += 1

    return result, matchR


# Graph representation (Adjacency List)
# graph[u] = list of jobs applicant u can take

graph = [
    [0, 1],  # A1 -> J1, J2
    [0],     # A2 -> J1
    [1, 2]   # A3 -> J2, J3
]

m = 3  # number of jobs
n = 3  # number of applicants

max_match, matchR = max_bipartite_matching(graph, m, n)

print("Maximum Matching Size =", max_match)

print("Matching:")
for j in range(m):
    if matchR[j] != -1:
        print(f"A{matchR[j]+1} – J{j+1}")
