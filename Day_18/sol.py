pInput = [
    (line.strip().split(" ")[0], int(line.strip().split(" ")[1]))
    for line in open("input.txt", "r")
]


def readjustMap(map, option, offset):
    if option == "rr":
        for c in range(len(map)):
            for _ in range(offset):
                map[c].append(0)
    elif option == "rl":
        for c in range(len(map)):
            for _ in range(offset):
                map[c].insert(0, 0)
    elif option == "cu":
        for _ in range(offset):
            map.insert(0, [0] * len(map[0]))
    elif option == "cd":
        for _ in range(offset):
            map.append([0] * len(map[0]))
    else:
        raise ValueError("Something is wrong. Wrong option number")
    return map

def isOOB(y, x, map):
    return not (0 <= y < len(map) and 0 <= x < len(map[0]))


def cardinalBFS(y, x, pmap):
    closed = set()
    open = [(y, x)]
    while True:
        inClosed = False
        if len(open) == 0:
            return closed
        coord = open.pop()
        if coord in closed:
            continue
        closed.add((coord[0], coord[1]))
        for next in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (
                not isOOB(coord[0] + next[0], coord[1] + next[1], pmap)
                and pmap[coord[0] + next[0]][coord[1] + next[1]]
                == pmap[coord[0]][coord[1]]
            ):
                open.append((coord[0] + next[0], coord[1] + next[1]))


 

def solve(pMap):
    pointer = [0, 0]
    for dir, steps in pInput:
        if dir == "R":
            if pointer[1] + steps >= len(pMap[pointer[0]]):
                pMap = readjustMap(
                    pMap, "rr", pointer[1] + steps - len(pMap[pointer[0]]) + 1
                )
            for _ in range(steps):
                pointer[1] = pointer[1] + 1
                pMap[pointer[0]][pointer[1]] = 1
        elif dir == "L":
            if pointer[1] - steps < 0:
                pMap = readjustMap(pMap, "rl", 0 - (pointer[1] - steps))
            for _ in range(steps):
                pointer[1] = pointer[1] - 1
                pMap[pointer[0]][pointer[1]] = 1
        elif dir == "U":
            if pointer[0] - steps < 0:
                pMap = readjustMap(pMap, "cu", 0 - (pointer[0] - steps))
            for _ in range(steps):
                pointer[0] = pointer[0] - 1
                pMap[pointer[0]][pointer[1]] = 1
        elif dir == "D":
            if pointer[0] + steps > len(pMap):
                pMap = readjustMap(pMap, "cd", pointer[0] + steps - len(pMap) + 1)
            for _ in range(steps):
                pointer[0] = pointer[0] + 1
                pMap[pointer[0]][pointer[1]] = 1
    
   
    pMap.append([0] * len(pMap[0]))
    pMap.insert(0, [0] * len(pMap[0]))
    for i, row in enumerate(pMap):
        pMap[i].append(0)
        pMap[i].insert(0, 0)

    start = (0, 0)
    closed = cardinalBFS(0, 0, pMap)
    
    for y, x in closed:
        pMap[y][x] = 2

    with open('final_map.txt', 'w' ) as f:
        for row in pMap:
            f.write(''.join([str(x) for x in row]) + '\n')


    res = 0
    for row in pMap:
        res += row.count(1)
        res += row.count(0)
    
    return res
    

print(solve([[0]]))
