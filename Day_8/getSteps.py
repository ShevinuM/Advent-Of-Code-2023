def getSteps(index, element, COMMANDS, map):
    count = 0
    while (not element.endswith('Z')):
        element = map.get(element)[COMMANDS[index]]
        index = (index+1)%len(COMMANDS)
        count = count + 1
    return count