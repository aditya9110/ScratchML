import numpy as np
import math

def printOutput(iteration, u, v):
    print('Iteration ' + str(iteration) + ': ')
    print('{:<8} {:<12} {:<8}'.format('Nodes', 'Hub Score', 'Authority Score'))
    uDict, vDict = {}, {}
    for i in range(len(u)):
        uDict[chr(65 + i)] = u[i]
        vDict[chr(65 + i)] = v[i]
        print('{:<8} {:<12} {:<8}'.format(chr(65+i), str(round(u[i], 4)), str(round(v[i], 4))))
    uDictSorted = sorted(uDict.items(), key=lambda item: item[1])
    uDictSorted = {k: v for k, v in uDictSorted}
    vDictSorted = sorted(vDict.items(), key=lambda item: item[1])
    vDictSorted = {k: v for k, v in vDictSorted}
    print()
    print('Hub Rank: ' + str(list(uDictSorted.keys())[::-1]))
    print('Authority Rank: ' + str(list(vDictSorted.keys())[::-1]))
    print()

n = int(input('Enter numbers of vertices: '))
'''
0 1 1 1
0 0 1 1 
1 0 0 1
0 0 0 1

0 1 0 0
0 0 1 0
0 1 0 1
1 0 0 0
'''
mat = []
print('Enter the adjacency matrix for the graph')
for i in range(n):
    mat.append(list(map(int, input().split())))

k = int(input('Enter numbers of iterations (k): '))
matT = np.transpose(mat)

v = np.ones(n)

v = np.dot(matT, v)
u = np.dot(mat, v)

printOutput(1, u, v)
for i in range(k-1):
    demU, demV = 0, 0
    for j in range(n):
        demU += (u[j]) ** 2
        demV += (v[j]) ** 2
    for j in range(n):
        u[j] /= math.sqrt(demU)
        v[j] /= math.sqrt(demV)
    printOutput(i+2, u, v)

