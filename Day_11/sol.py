from itertools import combinations


def parseInput(filename, offset):
    pInput = [list(line.replace("\n", "")) for line in open(filename, "r")]
    new_rows = {}
    new_cols = {}
    for r in range(len(pInput)):
        new_rows[r] = r
    for c in range(len(pInput[0])):
        new_cols[c] = c

    # offset rows
    for r in range(len(pInput)):
        line = pInput[r]
        if not "#" in line:
            for nr in range(r + 1, len(pInput)):
                new_rows[nr] = new_rows[nr] + offset

    # offset columns
    for c in range(len(pInput[0])):
        found = False
        for r in range(len(pInput)):
            if pInput[r][c] == "#":
                found = True
                break
        if not found:
            for nc in range(c + 1, len(pInput[0])):
                new_cols[nc] = new_cols[nc] + offset

    # replace # with number
    n = 1
    coords = {}
    for i in range(len(pInput)):
        while "#" in pInput[i]:
            index = pInput[i].index("#")
            pInput[i][index] = str(n)
            coords[n] = [new_rows[i], new_cols[index]]  # [row, col]
            n += 1

    return pInput, coords


def getSum(coords):
    # form combinations
    keys = list(coords.keys())
    combos = list(combinations(keys, 2))

    sum = 0
    for combo in combos:
        r1 = coords.get(combo[0])[0]
        c1 = coords.get(combo[0])[1]
        r2 = coords.get(combo[1])[0]
        c2 = coords.get(combo[1])[1]
        sum += abs(r1 - r2) + abs(c1 - c2)
    return sum


# Part 1
pInput, coords = parseInput("input.txt", 1)
print("Part 1 -> ", getSum(coords))

# Part 2
pInput, coords = parseInput("input.txt", 1000000 - 1)
print("Part 2 -> ", getSum(coords))
