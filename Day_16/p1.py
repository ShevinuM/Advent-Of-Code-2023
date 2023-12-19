from collections import deque

pInput = [list(line.replace("\n", "")) for line in open("input.txt", "r")]


def isOOB(y, x):
    if 0 <= y < len(pInput) and 0 <= x < len(pInput[0]):
        return False
    return True


def getNextCoords(dir, y, x):
    new_y = y
    new_x = x
    ret = []
    # if the current coordinate is a '.' then the same direction
    if pInput[y][x] == ".":
        if dir == ">":
            new_x += 1
        elif dir == "<":
            new_x -= 1
        elif dir == "A":
            new_y -= 1
        elif dir == "V":
            new_y += 1
        if not isOOB(new_y, new_x):
            return [(dir, new_y, new_x)]

    elif pInput[y][x] == "-":
        if dir == ">":
            if not isOOB(new_y, new_x + 1):
                ret.append((dir, new_y, new_x + 1))
        elif dir == "<":
            if not isOOB(new_y, new_x - 1):
                ret.append((dir, new_y, new_x - 1))
        else:
            if not isOOB(new_y, new_x + 1):
                ret.append((">", new_y, new_x + 1))
            if not isOOB(new_y, new_x - 1):
                ret.append(("<", new_y, new_x - 1))

    elif pInput[y][x] == "|":
        if dir == "A":
            if not isOOB(new_y - 1, new_x):
                ret.append((dir, new_y - 1, new_x))
        elif dir == "V":
            if not isOOB(new_y + 1, new_x):
                ret.append((dir, new_y + 1, new_x))
        else:
            if not isOOB(new_y - 1, new_x):
                ret.append(("A", new_y - 1, new_x))
            if not isOOB(new_y + 1, new_x):
                ret.append(("V", new_y + 1, new_x))

    elif pInput[y][x] == "\\":
        if dir == "A":
            if not isOOB(new_y, new_x - 1):
                ret.append(("<", new_y, new_x - 1))
        elif dir == "V":
            if not isOOB(new_y, new_x + 1):
                ret.append((">", new_y, new_x + 1))
        elif dir == ">":
            if not isOOB(new_y + 1, new_x):
                ret.append(("V", new_y + 1, new_x))
        elif dir == "<":
            if not isOOB(new_y - 1, new_x):
                ret.append(("A", new_y - 1, new_x))

    elif pInput[y][x] == "/":
        if dir == "A":
            if not isOOB(new_y, new_x + 1):
                ret.append((">", new_y, new_x + 1))
        elif dir == "V":
            if not isOOB(new_y, new_x - 1):
                ret.append(("<", new_y, new_x - 1))
        elif dir == "<":
            if not isOOB(new_y + 1, new_x):
                ret.append(("V", new_y + 1, new_x))
        elif dir == ">":
            if not isOOB(new_y - 1, new_x):
                ret.append(("A", new_y - 1, new_x))

    return ret


dq = deque()
dq.append((">", 0, 0))
visited_states = set()
visited_locs = set()
while dq:
    item = dq.popleft()
    if item in visited_states:
        continue
    dir = item[0]
    y = item[1]
    x = item[2]
    visited_states.add(item)
    visited_locs.add((y, x))
    successors = getNextCoords(dir, y, x)
    for s in successors:
        dq.append(s)

print(len(visited_locs))
