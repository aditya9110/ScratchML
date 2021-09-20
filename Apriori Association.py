import numpy as np
from itertools import combinations

# to create combinations of each items in the list
def makeCombinations(curr, k):
    newCurr = []
    comb = combinations(curr, k)
    for i in comb:
        temp = []
        for x in list(i):
            temp += x
        newCurr.append(list(set(temp)))
    return newCurr


# to find the support count of each item and whether it qualifies the min support count
def eligibleItems(curr):
    countMap = {}
    for items in curr:
        countMap[curr.index(items)] = 0
        for transaction in data:
            flag = 1
            for item in items:
                if item not in transaction:
                    flag = 0
            if flag:
                countMap[curr.index(items)] += 1
    newCurr = []
    for i in countMap:
        if countMap[i] >= minSupportCount:
            newCurr.append(curr[i])
    return newCurr


minSupportCount = int(input('Enter Minimum Support Count: '))
# minSupportCount = 3
data = [['mobile', 'backcase', 'headphones'], ['mobile', 'earphones'], ['mobile', 'earphones', 'charger'],
        ['mobile', 'backcase', 'powerbank'], ['earphones', 'headphones', 'usbcable'],
        ['mobile', 'earphones', 'powerbank'], ['powerbank', 'usbcable', 'charger'],
        ['mobile', 'backcase', 'powerbank', 'charger']]
#data = [['I1','I2','I5'], ['I2','I4'], ['I2','I3'], ['I1', 'I2','I4'],
#         ['I1', 'I3'], ['I2', 'I3'], ['I1', 'I3'], ['I1', 'I2','I3','I5'], ['I1', 'I2','I3']]
uniqueWords = []
for i in range(len(data)):
    uniqueWords += list(data[i])
uniqueWords = list(set(uniqueWords))
uniqueWords = np.reshape(uniqueWords, (len(uniqueWords), 1))
curr = uniqueWords.tolist()

curr = eligibleItems(curr)
k = 1
print('L' + str(k) + ': ')
for i in curr:
    print(i)
prev = []
while curr:
    prev = curr
    k += 1
    curr = makeCombinations(curr, k)

    curr = eligibleItems(curr)
    print('L' + str(k) + ': ')
    for i in curr:
        print(i)
print('\n')
print('Final frequent itemsets: ')
for i in prev:
    print(i)
