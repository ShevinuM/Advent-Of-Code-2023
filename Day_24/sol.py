from itertools import combinations


def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x1 == x2 and y1 == y2) or (x3 == x4 and y3 == y4):
        return False, (None, None)
    denominator = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)

    if denominator == 0:
        return False, (None, None)

    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denominator
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denominator

    nX = x1 + ua * (x2 - x1)
    nY = y1 + ua * (y2 - y1)

    if (
        ua <= 0
        or ub <= 0
        or nX < 200000000000000
        or nX > 400000000000000
        or nY < 200000000000000
        or nY > 400000000000000
    ):
        return False, (None, None)
    return True, (nX, nY)


pInput = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().replace(" ", "").replace("@", ",")
        x, y, z, vx, vy, vz = line.split(",")
        pInput.append(((int(x), int(y)), (int(vx), int(vy))))

res = 0
combinations = list(combinations(pInput, 2))
for ((sx1, sy1), (vx1, vy1)), ((sx2, sy2), (vx2, vy2)) in combinations:
    t = 2
    px1 = sx1 + vx1 * t
    py1 = sy1 + vy1 * t
    px2 = sx2 + vx2 * t
    py2 = sy2 + vy2 * t
    intersects, (x, y) = intersect(sx1, sy1, px1, py1, sx2, sy2, px2, py2)
    if intersects:
        res += 1

print(res)
