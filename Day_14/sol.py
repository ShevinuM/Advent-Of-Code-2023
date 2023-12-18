def parseInput(filename):
    input = [list(line.strip().replace("\n", "")) for line in open(filename, "r")]
    transposed = list(map(list, zip(*input)))
    return input, transposed


def tilt(input, transposed):
    for i in range(len(transposed)):
        l = 0
        while transposed[i][l] == "#":
            l += 1
        r = l + 1
        c = 1 if transposed[i][l] == "O" else 0
        while r <= len(transposed[i]):
            if r == len(transposed[i]) or transposed[i][r] == "#":
                for j in range(r - l):
                    if j < c:
                        transposed[i][l + j] = "O"
                    else:
                        transposed[i][l + j] = (
                            "." if transposed[i][l + j] == "O" else transposed[i][l + j]
                        )
                if r >= len(transposed[i]) - 1:
                    break
                else:
                    l = r + 1
                    while l < len(transposed[i]) and transposed[i][l] == "#":
                        l += 1
                    if l >= len(transposed[i]):
                        break
                    r = l + 1
                    c = 1 if transposed[i][l] == "O" else 0
            else:
                if transposed[i][r] == "O":
                    c += 1
                r += 1
    return list(map(list, zip(*transposed)))[::-1]


def calcLoad(input):
    load = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "O":
                load += r + 1
    return load


input, transposed = parseInput("input.txt")
tilted_input = tilt(input, transposed)
print(calcLoad(tilted_input))