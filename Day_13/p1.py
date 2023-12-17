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
                int_val = int(bs, 2)
                rows[e][i] = int_val
            for i in range(len(cols[e])):
                bs = "".join(cols[e][i])
                int_val = int(bs, 2)
                cols[e][i] = int_val
        return rows, cols, len(rows)


# rows = [[358, 90, 385, 385, 90, 102, 346], [281, 265, 103, 502, 502, 103, 265]]
# cols = [[89, 24, 103, 66, 37, 37, 66, 103, 24], [109, 12, 30, 30, 76, 97, 30, 30, 115]]
def getSum(item):
    l = 0
    r = 1
    s = l
    while r < len(item):
        if item[l] != item[r]:
            l = s + 1
            r = l + 1
            s = l
        else:
            l -= 1
            r += 1
            if l < 0 or r >= len(item):
                return s + 1
    return 0


rows, cols, nInputs = parseInput("input.txt")
# print(rows)
# print(cols)
res = 0
for i in range(nInputs):
    row = rows[i]
    col = cols[i]
    row_sum = getSum(row)
    col_sum = getSum(col)
    if row_sum != 0 and col_sum != 0:
        raise Exception("Invalid input")
    res += 100 * row_sum + col_sum
print(res)
