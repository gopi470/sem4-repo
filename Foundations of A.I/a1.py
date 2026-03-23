g = {
    'A': ['B', 'C'],
    'B': ['D', 'G'],
    'C': ['B', 'D'],
    'D': ['G'],
    'G': []
}

count = {}
for i in g:
    count[i] = 0


def iteratorsuccessor(node):
    i = 0
    while i < len(g[node]):
        yield g[node][i]
        i += 1


def enumerate_exhaustive(p, node):
    p.append(node)
    count[node] += 1

    i = 0
    while i < len(p):
        print(p[i], end=" ")
        i += 1
    print()

    for i in iteratorsuccessor(node):
        enumerate_exhaustive(p, i)

    p.pop()


def enumerate_search(p, node):
    p.append(node)

    if node == 'G':
        yield p[:]
    else:
        for i in iteratorsuccessor(node):
            yield from enumerate_search(p, i)

    p.pop()


print("DAG:", g, end="\n\n")

print("Exhaustive Enumeration:")
enumerate_exhaustive([], 'A')

print()
print("Path Counts:")
for i in count:
    print(i, ":", count[i])

# for key, value in count.items():
#     print(key, ":", value)

print()
print("Enumerate Search of the Goal Node:")

s = enumerate_search([], 'A')
while True:
    p = next(s, "End")
    if p == "End":
        break
    print(p)


# for p in enumerate_search([], 'A'):
#     print(p)

