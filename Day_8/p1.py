from parseInput import parseInput
from getSteps import getSteps

COMMANDS, map, start  = parseInput([], {}, [],  "input.txt")

print(getSteps(0, "AAA", COMMANDS, map))
