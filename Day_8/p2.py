from parseInput import parseInput
from math import lcm
from getSteps import getSteps

COMMANDS, map, start  = parseInput([], {}, [],  "input.txt")

cycles = []
for i in range(len(start)): cycles.append(getSteps(0, start[i], COMMANDS, map))

print(lcm(*cycles))

