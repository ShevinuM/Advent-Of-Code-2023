def calculateNextTerm(pInput):
    res = 0
    for item in pInput:
        item.append(0)
        struct = []
        struct.append(item)
        offSet = 0
        while not all(value == 0 for value in struct[-1]):
            nItem = [0] * len(item)
            for i in range(offSet, len(struct[-1])):
                if (i + 1) < len(item) - 1:
                    nItem[i + 1] = struct[-1][i + 1] - struct[-1][i]
            struct.append(nItem)
            offSet += 1
        for i in range(len(struct) - 1, -1, -1):
            if (i - 1) >= 0:
                struct[i - 1][-1] = struct[i - 1][-2] + struct[i][-1]
        res += struct[0][-1]
    return res


pInput = [list(map(int, line.split()[:])) for line in open("input.txt", "r")]

print("Part 1 -> ", calculateNextTerm(pInput))

pInput = [item[::-1] for item in pInput]

print("Part 2 -> ", calculateNextTerm(pInput))
