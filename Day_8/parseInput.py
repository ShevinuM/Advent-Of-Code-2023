def parseInput(COMMANDS, map, start, file):
    with open(file, 'r') as f:
        pivot = False
        for line in f:
            if (not pivot):
                line = line.replace("L", "0").replace("R", "1").replace("\n", "")
                COMMANDS = [int(x) for x in list(line)]
                pivot = True
            elif (line.strip() == ""):
                continue
            else:
                parts = line.split(" = ") #['AAA', '(BBB, CCC)']
                if (parts[0].endswith("A")): start.append(parts[0])
                parts[1] = parts[1].replace("(", "").replace(")", "").replace("\n", "") #['AAA', 'BBB, CCC']
                parts[1] = parts[1].split(", ") #['AAA', ['BBB', 'CCC']]
                map[parts[0]] = parts[1]
    return COMMANDS, map, start