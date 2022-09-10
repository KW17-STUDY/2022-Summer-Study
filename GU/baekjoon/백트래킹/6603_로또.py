#37
from itertools import combinations

def printForm(comb):
    for i in comb:
        print(i, end = ' ')
    print()

while True:
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        break
    k, test_case = inputs[0], inputs[1:]
    for i in combinations(test_case, 6):
        printForm(i)
    print()

