pInput = [list(map(int, line.split()[1:])) for line in open('input.txt', 'r')]

# Part 1
res = 0
for i in range(len(pInput[0])):
    c = 0
    for i2 in range (pInput[0][i]):
        d = (pInput[0][i] - i2) * i2
        if d > pInput[1][i]: c = c + 1
    res = c if res == 0 else res * c
print(res)

# Part 2
pInput = [int(''.join(line.split()[1:])) for line in open('test-input.txt', 'r')]
c = 0
for i in range (pInput[0]):
    d = (pInput[0] - i) * i
    if d > pInput[1]: c = c + 1
print(c)