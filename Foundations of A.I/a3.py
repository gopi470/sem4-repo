def displayMaze(m):
    i = 0
    while i < len(m):
        print("|", end="")
        j = 0
        while j < len(m[i]):
            if m[i][j] == "":
                print(" ", end="|")
            else:
                print(m[i][j], end="|")
            j += 1
        print()
        i += 1


def neighbours(c):
    x = c[0]
    y = c[1]

    idx = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    n = []

    i = 0
    while i < len(idx):
        xi = idx[i][0]
        yi = idx[i][1]

        if xi >= 0 and yi >= 0 and xi < len(maze) and yi < len(maze[0]):
            if maze[xi][yi] == "":
                n.append((xi, yi))
        i += 1

    return n


def move_direction(c, n):
    d = (c[0] - n[0], c[1] - n[1])

    if d == (0, 1):
        return "L"
    elif d == (0, -1):
        return "R"
    elif d == (-1, 0):
        return "D"
    else:
        return "U"


def depth_first_search(c, m):
    explored.add(c)

    if c == (len(maze)-1, len(maze[0])-1):
        return True

    i = 0
    n = neighbours(c)
    while i < len(n):
        if n[i] not in explored:
            m = move_direction(c, n[i])
            parent[n[i]] = (c, m)
            if depth_first_search(n[i], m):
                return True
        i += 1

    return False


def display_path(c):
    if c != None:
        if c in parent and parent[c][0] != None:
            display_path(parent[c][0])
        print("Move:", parent[c][1], "->", c, end=" - ")
        maze[c[0]][c[1]] = "X"


maze = [
    ["", "", "W", "", "", "", "", "", "", "W", "", "W", "W"],
    ["", "", "", "", "W", "W", "W", "", "W", "W", "", "", ""],
    ["W", "W", "", "", "", "W", "", "", "", "W", "W", "W", ""],
    ["W", "", "", "", "W", "W", "", "W", "", "", "", "", ""],
    ["", "", "", "W", "W", "", "", "", "", "W", "", "W", "W"],
    ["", "W", "W", "", "", "W", "W", "W", "W", "W", "", "", ""],
    ["", "", "", "", "W", "W", "", "", "", "", "", "W", ""],
    ["", "W", "", "W", "W", "W", "W", "W", "W", "W", "W", "W", ""],
    ["", "W", "", "", "", "", "W", "", "", "", "", "W", "W"],
    ["", "W", "W", "", "W", "", "", "", "W", "", "", "", ""],
    ["W", "W", "", "", "", "W", "W", "", "W", "W", "", "W", ""],
    ["", "", "", "", "W", "W", "", "", "", "W", "", "W", ""]
]

explored = set()
parent = {(0, 0): (None, "X")}

print("Maze:")
displayMaze(maze)

print()
print("DFS Search:")
depth_first_search((0, 0), "X")

print()
print("Path:")
display_path((11, 12))
print("end")

print()
print("Marked Maze:")
displayMaze(maze)
