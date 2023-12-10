import sys
def checkSeed(m):
    key = m
    for lst in [htl, tth, ltt, wtl, ftw, stf, sts]:
        for item in lst:
            if item[0] <= key < item[0] + item[2]:
                n = abs(item[0] - key)
                key = item[1] + n
                break
    for i in range(0, len(seeds), 2):
        if seeds[i] <= key < seeds[i] + seeds[i + 1]:
            return True
    return False


with open("input.txt", "r") as file:
    lines = file.read().split("\n\n")

plist = [
    [
        list(map(int, filter(None, sub_line.split(":")[-1].strip().split(" "))))
        for sub_line in line.split("\n")
    ]
    for line in lines
]

seeds = plist[0][0]

sts = []
for i in range(1, len(plist[1])):
    sts.append(plist[1][i])

stf = []
for i in range(1, len(plist[2])):
    stf.append(plist[2][i])

ftw = []
for i in range(1, len(plist[3])):
    ftw.append(plist[3][i])

wtl = []
for i in range(1, len(plist[4])):
    wtl.append(plist[4][i])

ltt = []
for i in range(1, len(plist[5])):
    ltt.append(plist[5][i])

tth = []
for i in range(1, len(plist[6])):
    tth.append(plist[6][i])

htl = []
for i in range(1, len(plist[7])):
    htl.append(plist[7][i])

for m in range(sys.maxsize):
    if checkSeed(m):
        print(m)
        break
