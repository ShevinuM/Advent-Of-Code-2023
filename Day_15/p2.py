def parseInput(filename):
    with open(filename, "r") as f:
        pInput = [
            [list(entry)[0:-2], list(entry)[-2], list(entry)[-1]]
            for entry in f.read().replace("\n", "").replace("-", "- ").split(",")
        ]
        return pInput


def hash(entry):
    res = 0
    for chr in entry:
        res += ord(chr)
        res *= 17
        res %= 256
    return res


def createMap(pInput):
    map = {}
    for i in range(len(pInput)):
        label = pInput[i][0]
        fl = pInput[i][2]
        box_no = hash(label)
        if pInput[i][1] == "-":
            if box_no in map:
                for l in range(len(map[box_no])):
                    lens = map[box_no][l]
                    if lens[0] == label:
                        map[box_no].pop(l)
                        if len(map[box_no]) == 0:
                            del map[box_no]
                        break
        else:
            if box_no in map:
                for l in range(len(map[box_no])):
                    lens = map[box_no][l]
                    if lens[0] == label:
                        map[box_no][l][1] = fl
                        break
                else:
                    map[box_no].append([label, fl])
            else:
                map[box_no] = [[label, fl]]
    return map


def solve(box_map):
    res = 0
    for box_no, labels in box_map.items():
        for slot in range(len(labels)):
            res = res + (box_no + 1) * (slot + 1) * int(labels[slot][1])
    return res


pInput = parseInput("input.txt")
box_map = createMap(pInput)
print(solve(box_map))
