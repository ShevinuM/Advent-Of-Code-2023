from heapq import heappush, heappop

pInput = [[int(char) for char in list(line.strip())] for line in open("input.txt", "r")]
width, height = len(pInput[0]), len(pInput)

MAX_STEPS = 3
MIN_STEPS = 0


def maxStepsReached(steps):
    return steps > MAX_STEPS


def isOOB(y, x):
    return not (0 <= y < len(pInput) and 0 <= x < len(pInput[0]))


def expand_helper(node, dy, dx, dir, res):
    new_y = node[1] + dy
    new_x = node[2] + dx
    if isOOB(new_y, new_x) or (dir == node[3] and maxStepsReached(node[4] + 1)):
        return res
    if dir == node[3]:
        res.append((node[0] + pInput[new_y][new_x], new_y, new_x, dir, node[4] + 1))
        return res
    elif node[4] >= MIN_STEPS:
        res.append((node[0] + pInput[new_y][new_x], new_y, new_x, dir, 1))
        return res
    return res


def expand(node):
    res = []
    if node[3] == ">":
        for dy, dx, dir in [[0, 1, ">"], [-1, 0, "A"], [1, 0, "V"]]:
            res = expand_helper(node, dy, dx, dir, res)
    elif node[3] == "<":
        for dy, dx, dir in [[0, -1, "<"], [-1, 0, "A"], [1, 0, "V"]]:
            res = expand_helper(node, dy, dx, dir, res)
    elif node[3] == "A":
        for dy, dx, dir in [[-1, 0, "A"], [0, 1, ">"], [0, -1, "<"]]:
            res = expand_helper(node, dy, dx, dir, res)
    elif node[3] == "V":
        for dy, dx, dir in [[1, 0, "V"], [0, 1, ">"], [0, -1, "<"]]:
            res = expand_helper(node, dy, dx, dir, res)
    return res


def ucs():
    closed = set()
    open = []
    heappush(open, (0, 0, 0, ">", 0))

    while open:
        node = heappop(open)
        if (
            node[1] == height - 1
            and node[2] == width - 1
            and (MIN_STEPS <= node[4] <= MAX_STEPS)
        ):
            return node[0]
        if (node[1], node[2], node[3], node[4]) in closed:
            continue
        closed.add((node[1], node[2], node[3], node[4]))
        successors = expand(node)
        for i in range(len(successors)):
            heappush(open, successors[i])

    return -1


# Part 1
print("Part 1 -> ", ucs())

# Part 2
MAX_STEPS = 10
MIN_STEPS = 4
print("Part 2 -> ", ucs())
