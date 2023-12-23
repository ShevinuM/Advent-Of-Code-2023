import sys

sys.setrecursionlimit(2500)

pInput = [list(line.strip()) for line in open("input.txt")]

w, h = len(pInput[0]), len(pInput)

start = (0, pInput[0].index("."))
end = (h - 1, pInput[-1].index("."))
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


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


def DFS(y, x, steps, closed, max_steps):
    if (y, x) == end:
        return steps
    if (y, x) in closed:
        return
    closed.add((y, x))
    if (y, x) != end:
        successors = expand(y, x, steps)
        for newY, newX, newSteps in successors:
            s = DFS(newY, newX, newSteps, closed.copy(), max_steps)
            max_steps = s if s is not None and s > max_steps else max_steps
    return max_steps


print(DFS(start[0], start[1], 0, set(), -1))
