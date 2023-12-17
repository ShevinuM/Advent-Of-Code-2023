def parseInput(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

        # Create a list containing each input and it's corresponding rows
        rows = []
        temp_list = []
        for line in lines:
            if line != '':
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

        return rows, cols, len(rows)

def hash_item(lst):
    lst_str = ''.join(lst)
    return hash(lst_str)

def getSum(item, multiplier):
    stack = []
    start_i = -1
    start = False
    x = 1
    for i, r in enumerate(item):
        if i == 0: continue

        if not start and hash_item(r) == hash_item(item[i-1]):
            start = True
            start_i = i
            x+=1
            if (start_i-x < 0): break
            continue

        if start and hash_item(r) == hash_item(item[start_i - x]):
            x+=1
            if (start_i-x < 0): break
            continue

        if hash_item(item[i-1]) != hash_item(r) and start:
            start = False
            start_i = -1
            x = 1

    if not start: return 0

    return start_i*multiplier

rows, cols, nInputs = parseInput('input.txt')

print(rows)

res = 0
for i in range(nInputs):
    res += getSum(rows[i], 100) + getSum(cols[i], 1)

print(res)

def getSum():
    res = 0
    for i in range(nInputs):
        res += getSum(rows[i], 100) + getSum(cols[i], 1)
    return res


def getSum():
    res = 0
    for i in range(nInputs):
        res += getSum(rows[i], 100) + getSum(cols[i], 1)
    return res

def getSum():
    res = 0
    for i in range(nInputs):
        res += getSum(rows[i], 100) + getSum(cols[i], 1)
    return res
