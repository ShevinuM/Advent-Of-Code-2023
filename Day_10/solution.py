"""
    1. Parse the input into a list of lists
    2. Find the starting point
    3. Create a class for a node
        node.value = hashed index
        node.next = [list containing all the nodes it can go next]
        node.index = [y, x] index
        node.dist = distance from starting node
    4. Initialize starting node
"""

from collections import deque

def printMap(input):
    for y, row in enumerate(input):
        print(''.join(row))

def findStart(pInput):
    for y, row in enumerate(pInput):
        for x, element in enumerate(row):
            if element == "S":
                return y, x


def changeStart(sY, sX, pInput):
    n = s = e = w = False
    for dir in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        nY = sY + dir[0]
        nX = sX + dir[1]
        if nY >= len(pInput) or nX >= len(pInput[0]) or nY < 0 or nX < 0:
            continue
        if dir == [0, 1] and pInput[nY][nX] in ["-", "7", "J"]:
            e = True
        elif dir == [0, -1] and pInput[nY][nX] in ["-", "F", "L"]:
            w = True
        elif dir == [-1, 0] and pInput[nY][nX] in ["|", "7", "F"]:
            n = True
        elif dir == [1, 0] and pInput[nY][nX] in ["|", "L", "J"]:
            s = True
    if n and s:
        return "|"
    if e and w:
        return "-"
    if n and e:
        return "L"
    if n and w:
        return "J"
    if s and w:
        return "7"
    if s and e:
        return "F"
    return "."


def get1D(y, x, height): return y * height + x


pInput = [list(line.replace("\n", "")) for line in open("test_input_4.txt", "r")]

sY, sX = findStart(pInput)

pInput[sY][sX] = changeStart(sY, sX, pInput)

h = len(pInput)
w = len(pInput[0])

dq = deque()
dq.append([sY, sX, 0])
visited = set()
max = 0
while dq:
    y, x, cd = dq.popleft()
    if cd > max:
        max = cd
    e = pInput[y][x]
    if get1D(y, x, h) in visited:
        continue

    visited.add(get1D(y, x, h))

    """
        | is a vertical pipe connecting north and south.
        - is a horizontal pipe connecting east and west.
        L is a 90-degree bend connecting north and east.
        J is a 90-degree bend connecting north and west.
        7 is a 90-degree bend connecting south and west.
        F is a 90-degree bend connecting south and east.
        . is ground; there is no pipe in this tile.
        S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
    """
    if e == "|":
        if 0 <= y + 1 < h:
            dq.append([y + 1, x, cd + 1])
        if 0 <= y - 1 < h:
            dq.append([y - 1, x, cd + 1])
    elif e == "-":
        if 0 <= x + 1 < w:
            dq.append([y, x + 1, cd + 1])
        if 0 <= x - 1 < w:
            dq.append([y, x - 1, cd + 1])
    elif e == "L":
        if 0 <= y - 1 < h:
            dq.append([y - 1, x, cd + 1])
        if 0 <= x + 1 < w:
            dq.append([y, x + 1, cd + 1])
    elif e == "J":
        if 0 <= y - 1 < h:
            dq.append([y - 1, x, cd + 1])
        if 0 <= x - 1 < w:
            dq.append([y, x - 1, cd + 1])
    elif e == "7":
        if 0 <= y + 1 < h:
            dq.append([y + 1, x, cd + 1])
        if 0 <= x - 1 < w:
            dq.append([y, x - 1, cd + 1])
    elif e == "F":
        if 0 <= y + 1 < h:
            dq.append([y + 1, x, cd + 1])
        if 0 <= x + 1 < w:
            dq.append([y, x + 1, cd + 1])

print(max-1)


# Part 2
for y, row in enumerate(pInput):
    for x, item in enumerate(row):
        hash = get1D(y, x, h)
        if hash in visited:
            pInput[y][x] = '#'


printMap(pInput)


    
