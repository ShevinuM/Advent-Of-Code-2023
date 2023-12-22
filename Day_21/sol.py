from collections import deque

pInput = []
with open('input.txt', 'r') as f:
    for line in f:
        line = list(line.strip().replace('.', '0').replace('#', '1').replace('S', '2'))
        line = [int(chr) for chr in line]
        pInput.append(line)

HEIGHT, WIDTH, START = len(pInput), len(pInput[0]), (0, 0, 0)
MAX_DEPTH = 64
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dp = {}

for y in range(HEIGHT):
    for x in range(WIDTH):
        if pInput[y][x] == 2:
            START = (y, x, 0)

def expand(y, x):  
    if (y, x) in dp:
        return dp.get((y,x))  
    ret = []
    for dy, dx in DIRS:
        newY = y + dy
        newX = x + dx
        if 0 <= newY < HEIGHT and 0 <= newX < WIDTH and pInput[newY][newX] != 1:
            ret.append((newY, newX))
    dp[(y,x)] = ret
    return ret


def BFS():  
    closed = set()
    open = deque([START])
    while open:
        y, x, d = open.popleft()
        if d > MAX_DEPTH:
            break
        if (y, x) in closed:
            continue
        closed.add((y, x))   
        if d % 2 == 0:
            pInput[y][x] = -1
        successors = expand(y, x)
        for newY, newX in successors:
            open.append((newY, newX, d + 1))

BFS()
res = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if pInput[y][x] == -1:
            res+=1
print(res)
