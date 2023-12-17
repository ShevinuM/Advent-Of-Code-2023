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

"""
    item -> ['101100110', '001011010', '110000001', '110000001', '001011010', '001100110', '101011010']
"""
def getSum(item):
    r = 1
    while r < len(item):
        # above -> ['101100110', '001011010', '110000001']
        # below -> ['110000001', '001011010', '001100110', '101011010']
        above = item[r-1::-1]
        below = item[r:]
        n = len(above) if len(above) < len(below) else len(below)
        # x, y ->  '110000001', '110000001'
        sum = 0 
        for x, y in zip(above[:n], below[:n]):
            # a, b -> '1', '1'
            for a, b in zip(x, y):
                if abs(int(a) - int(b)) == 1:
                    sum += 1
        if sum == 1: 
            return len(above) 
        r += 1
    return 0 

rows, cols, nInputs = parseInput("input.txt")
res = 0 
for i in range(nInputs):
    row = rows[i]
    col = cols[i]
    row_sum = getSum(row)
    col_sum = getSum(col)
    if row_sum != 0 and col_sum != 0:
        raise Exception("Invalid input")
    res += 100*row_sum + col_sum
print(res)
