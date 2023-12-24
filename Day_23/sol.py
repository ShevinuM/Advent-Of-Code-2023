pInput = [list(line.strip()) for line in open("input.txt")]

w, h = len(pInput[0]), len(pInput)

start = (0, pInput[0].index("."))
end = (h - 1, pInput[-1].index("."))
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def printGraph(graph):
    for node in graph:
        print(node, graph[node])


def isOOB(y, x):
    return not (0 <= y < h and 0 <= x < w)


def expand(y, x, steps):
    res = []
    for dy, dx in dirs:
        newY = y + dy
        newX = x + dx
        if not isOOB(newY, newX) and pInput[newY][newX] != "#":
            e = pInput[newY][newX]
            if e == ".":
                res.append((newY, newX, steps + 1))
            elif e == "^" and not isOOB(newY - 1, newX):
                res.append((newY - 1, newX, steps + 2))
            elif e == ">" and not isOOB(newY, newX + 1):
                res.append((newY, newX + 1, steps + 2))
            elif e == "v" and not isOOB(newY + 1, newX):
                res.append((newY + 1, newX, steps + 2))
            elif e == "<" and not isOOB(newY, newX - 1):
                res.append((newY, newX - 1, steps + 2))
            else:
                raise ValueError("Unknown character found")
    return res


graph = {}


def formGraph():
    nodes = set()
    nodes.add(start)
    nodes.add(end)

    for y, row in enumerate(pInput):
        for x, element in enumerate(row):
            neigh = 0
            for dy, dx in dirs:
                nY = y + dy
                nX = x + dx
                if not isOOB(nY, nX) and element != "#" and pInput[nY][nX] != "#":
                    neigh += 1
            if neigh > 2:
                nodes.add((y, x))

    adj_list = {node: {} for node in nodes}

    for sy, sx in nodes:
        open = [(sy, sx, 0)]
        closed = set()

        while open:
            y, x, s = open.pop()
            if (y, x) in closed:
                continue
            closed.add((y, x))
            if s != 0 and (y, x) in nodes:
                adj_list[(sy, sx)][(y, x)] = s
                continue
            successors = expand(y, x, s)
            for ny, nx, ns in successors:
                open.append((ny, nx, ns))

    return adj_list


closed = set()


def dfs(node):
    if node == end:
        return 0

    m = -float("inf")

    closed.add(node)
    for e in graph[node]:
        if e not in closed:
            m = max(m, dfs(e) + graph[node][e])
    closed.remove(node)

    return m


# Part 1
graph = formGraph()
print("Part 1 -> ", dfs(start))


# Part 2
pInput = [
    list(
        line.strip()
        .replace(">", ".")
        .replace("<", ".")
        .replace("^", ".")
        .replace("v", ".")
    )
    for line in open("input.txt")
]
graph = formGraph()
print("Part 2 -> ", dfs(start))
