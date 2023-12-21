pInput = [
    (line.strip().split(" ")[0], int(line.strip().split(" ")[1]))
    for line in open("test_input.txt", "r")
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
            map.append([0] * len(map))
    else:
        raise ValueError("Something is wrong. Wrong option number")
    return map


def isOOB(y, x):
    return not (0 <= y < len(map) and 0 <= x < len(map[0]))


def cardinalBFS(y, x):
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
                not isOOB(coord[0], coord[1])
                and map[coord[0] + next[0]][coord[1] + next[1]]
                == map[coord[0]][coord[1]]
            ):
                open.append((coord[0] + next[0], coord[1] + next[1]))


def computeSectors():
    sector_no = 1
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] != 0:
                continue
            sector_no += 1
            visited_coords = cardinalBFS(y, x)
            for vy, vx in visited_coords:
                map[vy][vx] = sector_no


def solve(map):
    pointer = [0, 0]
    for dir, steps in pInput:
        print(dir, steps)
        if dir == "R":
            if pointer[1] + steps >= len(map[pointer[0]]):
                map = readjustMap(map, "rr", pointer[1] + steps - len(map[pointer[0]]) + 1)
            for _ in range(steps):
                pointer[1] = pointer[1] + 1
                map[pointer[0]][pointer[1]] = 1
        elif dir == "L":
            if pointer[1] - steps < 0:
                map = readjustMap(map, "rl", 0 - (pointer[1] - steps))
            for _ in range(steps):
                pointer[1] = pointer[1] - 1
                map[pointer[0]][pointer[1]] = 1
        elif dir == "U":
            if pointer[0] - steps < 0:
                map = readjustMap(map, "cu", 0 - (pointer[0] - steps))
            for _ in range(steps):
                pointer[0] = pointer[0] - 1
                map[pointer[0]][pointer[1]] = 1
        elif dir == "D":
            if pointer[0] + steps > len(map):
                map = readjustMap(map, "cd", pointer[0] + steps - len(map))
            for _ in range(steps):
                pointer[0] = pointer[0] + 1
                map[pointer[0]][pointer[1]] = 1

    print(map)
    # computeSectors()


print(pInput)
solve([[0]])
