from copy import deepcopy
from heapq import heappush, heappop

pInput = [[int(char) for char in list(line.replace("\n", ""))] for line in open("input.txt", "r")]
width, height = len(pInput[0]), len(pInput)


def maxStepsReached(steps):
    return steps > 10

def isOOB(y, x):
   return not (0 <= y < len(pInput) and 0 <= x < len(pInput[0]))

def expand(node):
    res = []
    if node[3] == '>':
        for dy, dx, dir in [[0, 1, '>'], [-1, 0, 'A'], [1, 0, 'V']]:
            new_y = node[1] + dy 
            new_x = node[2] + dx 
            if isOOB(new_y, new_x):
                continue
            if dir == '>' and maxStepsReached(node[4] + 1):
                continue
            if dir == '>':
                res.append((node[0] + pInput[new_y][new_x], new_y, new_x, dir, node[4] + 1))
            else:
                if node[4] >= 4:
                    res.append((node[0] + pInput[new_y][new_x], new_y, new_x, dir, 1))
    elif node[3] == '<':
        for dy, dx, dir in [[0, -1, '<'], [-1, 0, 'A'], [1, 0, 'V']]:
            new_y = node[1] + dy 
            new_x = node[2] + dx 
            if isOOB(new_y, new_x):
                continue
            if dir == '<' and maxStepsReached(node[4] + 1):
                continue
            if dir == '<':
                res.append((node[0] + pInput[new_y][new_x], new_y, new_x, dir, node[4] + 1))
            else:
                if node[4] >= 4:
                    res.append((node[0] + pInput[new_y][new_x], new_y, new_x, dir, 1))
    elif node[3] == 'A':
        for dy, dx, dir in [[-1, 0, 'A'], [0, 1, '>'], [0, -1, '<']]:
            new_y = node[1] + dy 
            new_x = node[2] + dx 
            if isOOB(new_y, new_x):
                continue
            if dir == 'A' and maxStepsReached(node[4] + 1):
                continue
            if dir == 'A':
                res.append((node[0] + pInput[new_y][new_x], new_y, new_x, dir, node[4] + 1))
            else:
                if node[4] >= 4:
                    res.append((node[0] + pInput[new_y][new_x], new_y, new_x, dir, 1))
    elif node[3] == 'V':
        for dy, dx, dir in [[1, 0, 'V'], [0, 1, '>'], [0, -1, '<']]:
            new_y = node[1] + dy 
            new_x = node[2] + dx 
            if isOOB(new_y, new_x):
                continue
            if dir == 'V' and maxStepsReached(node[4] + 1):
                continue
            if dir == 'V':
                res.append((node[0] + pInput[new_y][new_x], new_y, new_x, dir, node[4] + 1))
            else:
                if node[4] >= 4:
                    res.append((node[0] + pInput[new_y][new_x], new_y, new_x, dir, 1))
    return res 


def ucs():
    closed = set()
    open = []
    heappush(open, (0, 0, 0, '>', 1))
    heappush(open, (0, 0, 0, 'V', 1))
    heappush(open, (0, 0, 0, 'A', 1))
    heappush(open, (0, 0, 0, '<', 1))

    while open:
        node = heappop(open)
        if node[1] == height - 1 and node[2] == width - 1 and node[4] >= 4: 
            return node[0]
        if (node[1], node[2], node[3], node[4]) in closed:
            continue
        closed.add((node[1], node[2], node[3], node[4]))
        successors = expand(node)
        for s in successors:
            heappush(open, s)
        

    return -1


print(ucs())
