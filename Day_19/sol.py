from re import split

wmap = {}
with open("workflows_test.txt", "r") as f:
    for line in f:
        parts = line.strip().replace("}", "").split("{")
        parts[1] = parts[1].split(",")
        for i in range(len(parts[1])):
            parts[1][i] = parts[1][i].split(":")
            if len(parts[1][i]) == 1:
                parts[1][i].insert(0, None)
            else:
                parts[1][i][0] = split("(?=[><])|(?<=[><])", parts[1][i][0])
                parts[1][i][0][-1] = int(parts[1][i][0][-1])
                parts[1][i][0] = tuple(parts[1][i][0])
            parts[1][i] = tuple(parts[1][i])
        wmap[parts[0]] = parts[1]

print(wmap)
ratings = []
with open("ratings_test.txt", "r") as f:
    for line in f:
        line = line.strip().replace("{", "").replace("}", "")
        parts = line.split(",")
        for i in range(len(parts)):
            parts[i] = int(parts[i].split("=")[1])
        parts = tuple(parts)
        ratings.append(parts)

res = 0
for x, m, a, s in ratings:
    curr = "in"
    while curr != "A" and curr != "R":
        print(curr)
        workflows = wmap.get(curr)
        print(workflows)
        for w in workflows:
            if w[0] is None:
                curr = w[1]
                break
            else:
                if w[0][1] == ">":
                    if w[0][0] == "x":
                        if x > w[0][2]:
                            curr = w[1]
                            break
                    elif w[0][0] == "m":
                        if m > w[0][2]:
                            curr = w[1]
                            break
                    elif w[0][0] == "a":
                        if a > w[0][2]:
                            curr = w[1]
                            break
                    elif w[0][0] == "s":
                        if s > w[0][2]:
                            curr = w[1]
                            break
                else:
                    if w[0][0] == "x":
                        if x < w[0][2]:
                            curr = w[1]
                            break
                    elif w[0][0] == "m":
                        if m < w[0][2]:
                            curr = w[1]
                            break
                    elif w[0][0] == "a":
                        if a < w[0][2]:
                            curr = w[1]
                            break
                    elif w[0][0] == "s":
                        if s < w[0][2]:
                            curr = w[1]
                            break
    if curr == "A":
        res += x + m + a + s

print(res)
