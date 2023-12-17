""" 
    1. Parse the input into an array of the form [["set", bid], .....]
    2. Create a function which compares two sets
    3. Use the custom comparator with Python's sort function to sort the list
    4. Iterate over the list and sum += (i+1) * (list[i][1])
 """

from collections import Counter
from functools import cmp_to_key

"""
    0 -> High Card
    1 -> One pair
    2 -> Two pair
    3 -> Three of a kind
    4 -> Full House
    5 -> Four of a kind
    6 -> Five of a kind
"""
def evalType(set):
    char_count = Counter(set)
    pairs = []
    for char, count in char_count.items(): # KK677
        pairs.append(count) # [2, 1, 2]

    c = Counter(pairs) # {1 : 1, 2 : 2}
    if (c.get(1) == 5): return 0
    if (c.get(2) == 1 and c.get(1) == 3): return 1
    if (c.get(2) == 2 and c.get(1) == 1): return 2
    if (c.get(3) == 1 and c.get(1) == 2): return 3
    if (c.get(3) == 1 and c.get(2) == 1): return 4
    if (c.get(4) == 1 and c.get(1) == 1): return 5
    if (c.get(5) == 1): return 6

def evalCard(card):
    if card == '2': return 0
    if card == '3': return 1
    if card == '4': return 2
    if card == '5': return 3
    if card == '6': return 4
    if card == '7': return 5
    if card == '8': return 6
    if card == '9': return 7
    if card == 'T': return 8
    if card == 'J': return 9
    if card == 'Q': return 10
    if card == 'K': return 11
    if card == 'A': return 12

def compare(set1, set2):
    # compare based on type
    t1 = evalType(set1)
    t2 = evalType(set2)
    if (t1 != t2): return t1 - t2

    # second ordering rule
    for i in range(5):
        e1 = evalCard(set1[i])
        e2 = evalCard(set2[i])
        if (e1 != e2): return e1 - e2
    else:
        return 0



with open('input.txt', 'r') as f:
    lst = [[line.split()[0], int(line.split()[1])] for line in f]

lst = sorted(lst, key=cmp_to_key(lambda x, y: compare(x[0], y[0])))
sum = 0
for i in range(len(lst)):
    sum += (i+1) * (lst[i][1])
print(sum)
