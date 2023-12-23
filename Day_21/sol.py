from collections import deque

pInput = []
with open('test_input.txt', 'r') as f:
    for line in f:
        line = list(line.strip().replace('.', '0').replace('#', '1').replace('S', '2'))
        line = [int(chr) for chr in line]
        pInput.append(line)

HEIGHT, WIDTH, START = len(pInput), len(pInput[0]), (0, 0, 0, 0)
MAX_DEPTH = 10 
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dp = {}

for y in range(HEIGHT):
    for x in range(WIDTH):
        if pInput[y][x] == 2:
            START = (y, x, 0, 0)

def expand(y, x, l):     
    ret = []
    for dy, dx in DIRS:
        newY = y + dy 
        newX = x + dx
        if not (0 <= newY < HEIGHT and 0 <= newX < WIDTH):
            newY = newY % HEIGHT
            newX = newX % WIDTH
            l+=1
        if pInput[newY][newX] != 1:
            ret.append((newY, newX, l))
    return ret


def BFS():
    res = 0
    closed = set()
    open = deque([START])
    while open:
        y, x, d, l = open.popleft()
        if d > MAX_DEPTH:
            return res
        if (y, x, l) in closed:
            continue
        closed.add((y, x, l))   
        if d % 2 == 0:
            res+=1
        successors = expand(y, x, l)
        for newY, newX, level in successors:
            open.append((newY, newX, d + 1, level))
    return res
print(BFS())
