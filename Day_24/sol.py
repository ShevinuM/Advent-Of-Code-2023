from itertools import combinations
import sympy as s


def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
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
pInput2 = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().replace(" ", "").replace("@", ",")
        x, y, z, vx, vy, vz = line.split(",")
        pInput.append(((int(x), int(y)), (int(vx), int(vy))))
        pInput2.append(((int(x), int(y), int(z)), (int(vx), int(vy), int(vz))))

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

print("Part 1 -> ", res)

# Part 2
eqs = []
srx, sry, srz, vrx, vry, vrz = s.symbols("srx, sry, srz, vrx, vry, vrz")
for (sx, sy, sz), (vx, vy, vz) in pInput2:
    eqs.append((srx - sx) * (vy - vry) - (sry - sy) * (vx - vrx))
    eqs.append((sry - sy) * (vz - vrz) - (srz - sz) * (vy - vry))
a = s.solve(eqs)
print(a[0][srx] + a[0][sry] + a[0][srz])
