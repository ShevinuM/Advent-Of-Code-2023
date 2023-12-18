def parseInput(filename):
    # Copilot, how do i read a single line file and split into a list by comma
    with open(filename, 'r') as f:
        pInput = [list(entry) for entry in f.read().replace("\n", "").split(',')]
        return pInput

def solve(pInput):
    res = 0
    for i in range(len(pInput)):
        curr = 0
        for chr in pInput[i]:
            curr += ord(chr)
            curr *= 17
            curr %= 256
        print(pInput[i], curr)
        res += curr
    return res

pInput = parseInput('input.txt')
print(solve(pInput))
