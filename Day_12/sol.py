from itertools import combinations
from re import findall

# Part 1
with open("test_input.txt", "r") as f:
    res = 0
    line_no = 1
    for line in f:
        print(line_no)
        parts = [
            line.replace("\n", "").split(" ")[0],
            [int(x) for x in line.replace("\n", "").split(" ")[1].split(",")],
        ]
        tot = sum(num for num in parts[1]) - parts[0].count("#")
        indices = [i for i, c in enumerate(parts[0]) if c == "?"]
        combos = list(combinations(indices, tot))
        for combo in combos:
            temp = list(parts[0])
            for i in indices:
                if i in combo:
                    temp[i] = "#"
                else:
                    temp[i] = "."
            temp_s = "".join(temp)
            clusters = findall("#+", temp_s)
            if len(clusters) != len(parts[1]):
                continue
            for i in range(len(clusters)):
                if len(clusters[i]) != parts[1][i]:
                    break
            else:
                res += 1
        line_no += 1
    print(res)
