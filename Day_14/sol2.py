def parseInput(filename):
    input = [list(line.strip().replace("\n", "")) for line in open(filename, "r")]
    transposed = list(map(list, zip(*input)))
    return input, transposed


def tilt(input, dir):
    if dir == "n" or dir == "s":
        transposed = list(map(list, zip(*input)))
    else:
        transposed = input

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
                        if dir == "n" or dir == "w":
                            transposed[i][l + j] = "O"
                        else:
                            transposed[i][r - j - 1] = "O"
                    else:
                        if dir == "n" or dir == "w":
                            transposed[i][l + j] = (
                                "."
                                if transposed[i][l + j] == "O"
                                else transposed[i][l + j]
                            )
                        else:
                            transposed[i][r - j - 1] = (
                                "."
                                if transposed[i][r - j - 1] == "O"
                                else transposed[i][r - j - 1]
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
    if dir == "n" or dir == "s":
        transposed = list(map(list, zip(*transposed)))

    return transposed


def calcLoad(input):
    load = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "O":
                load += len(input) - r
    return load


def split_array_on_value(arr, value):
    result = []
    current_subarray = []

    for item in arr:
        if item == value and current_subarray:
            # Append the current subarray to the result and start a new one
            result.append(current_subarray)
            current_subarray = []
        current_subarray.append(item)

    # Add the last subarray if it's not empty
    if current_subarray:
        result.append(current_subarray)

    return result


# Part 1
cache = {}
input, transposed = parseInput("input.txt")

tilted_input = tilt(input, "n")
print("Part 1 -> ", calcLoad(tilted_input))

dic = {}
cycle = []
for c in range(1000):
    for d in ["n", "w", "s", "e"]:
        tilted = tilt(input, d)
        input = tilted
    if (str(input)) in dic:
        cycle.append(calcLoad(input))
        continue
    else:
        dic[str(input)] = calcLoad(input)
        cycle.append(calcLoad(input))
split_arr = split_array_on_value(cycle, 93182)
pattern_length = len(split_arr[1])
v = 1000000000 - len(split_arr[0])
position = v % pattern_length
print("Part 2 -> ", split_arr[1][position - 1])

"""
for c in range(2000):
    found = False
    for d in ['n', 'w', 's', 'e']:
        grid_str = ''.join([''.join(row) for row in input])
        combined = f"{grid_str}_{d}"
        key =  hash(combined)      
        if key in cache:
            input = cache[key]
            found = True
        else:
            tilted = tilt(input, d)
            cache[key] = tilted
            input = tilted
    # if found: break
print("Part 2 -> ", calcLoad(input))
"""
