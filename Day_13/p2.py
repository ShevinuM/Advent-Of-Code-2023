def parseInput(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()

        # Create a list containing each input and it's corresponding rows
        rows = []
        temp_list = []
        for line in lines:
            if line != "":
                line = line.replace("#", "1").replace(".", "0")
                # Copilot, convert each char to in before appending to list
                temp_list.append(list(map(int, line)))
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
        return rows, cols, len(rows)


# rows = [[358, 90, 385, 385, 90, 102, 346], [281, 265, 103, 502, 502, 103, 265]]
# cols = [[89, 24, 103, 66, 37, 37, 66, 103, 24], [109, 12, 30, 30, 76, 97, 30, 30, 115]]
def getSum(item):
    return 0


rows, cols, nInputs = parseInput("test-input.txt")
print(rows)
print(cols)
res = 0
"""
for i in range(nInputs):
    row = rows[i]
    col = cols[i]
    row_sum = getSum(row)
    col_sum = getSum(col)
    if row_sum != 0 and col_sum != 0:
        raise Exception("Invalid input")
    res += 100*row_sum + col_sum
print(res)
"""
