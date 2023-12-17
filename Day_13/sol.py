def parseInput(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()

        # Create a list containing each input and it's corresponding rows
        rows = []
        temp_list = []
        for line in lines:
            if line != "":
                line = line.replace("#", "1").replace(".", "0")
                temp_list.append(list(line))
            else:
                rows.append(temp_list)
                temp_list = []
        if temp_list:
            rows.append(temp_list)

        # Create a list containing input and it's corresponding columns (transposed)
        cols = []
        for item in rows:
            item_transposed = list(map(list, zip(*item)))
            cols.append(item_transposed)

        for e in range(len(rows)):
            for i in range(len(rows[e])):
                bs = "".join(rows[e][i])
                rows[e][i] = bs
            for i in range(len(cols[e])):
                bs = "".join(cols[e][i])
                cols[e][i] = bs
        return rows, cols, len(rows)


def getAbove(item, part):
    r = 1
    while r < len(item):
        # above -> ['101100110', '001011010', '110000001']
        # below -> ['110000001', '001011010', '001100110', '101011010']
        above = item[r - 1 :: -1]
        below = item[r:]
        n = len(above) if len(above) < len(below) else len(below)
        if part == 2:
            sum = 0
            for x, y in zip(above[:n], below[:n]):
                # a, b -> '1', '1'
                for a, b in zip(x, y):
                    if abs(int(a) - int(b)) == 1:
                        sum += 1
            if sum == 1:
                return len(above)
        else:
            if above[:n] == below[:n]:
                return len(above)
        r += 1
    return 0


def getSum(filename, part):
    rows, cols, nInputs = parseInput(filename)
    res = 0
    for i in range(nInputs):
        row = rows[i]
        col = cols[i]
        row_sum = getAbove(row, part)
        col_sum = getAbove(col, part)
        if row_sum != 0 and col_sum != 0:
            raise Exception("Invalid input")
        res += 100 * row_sum + col_sum
    return res


print("Part 1: ", getSum("input.txt", 1))
print("Part 2: ", getSum("input.txt", 2))
