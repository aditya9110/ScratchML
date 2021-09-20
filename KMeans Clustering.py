import numpy as np
import random
import sys

# calculate clusters for each data points
def nearestCluster(num, meanvalues):
    dist = sys.maxsize
    currCluster = -1
    for i in range(len(meanvalues)):
        if abs(num - meanvalues[i]) < dist:
            dist = abs(num - meanvalues[i])
            currCluster = i
    return currCluster + 1

# update new mean values for each cluster
def newMean(cluster):
    mean = []
    for i in range(len(cluster)):
        mean.append(np.mean(cluster[i+1]))
    return mean

# printing clusters after each iteration
def printIter(i, cluster, k, meanvalues):
    print('Iteration #'+str(i))
    for curr in range(k):
        print('k'+str(curr+1)+': '+str(cluster[curr+1]))
    print()
    for mean in range(len(meanvalues)):
        print('Mean'+str(mean+1)+' = '+str(meanvalues[mean]))
    print()

# main code
n = int(input('Enter the number of elements: '))
print('Enter numbers: ')
arr = [int(x) for x in input().split()]
k = int(input('Enter the number of clusters: '))
meanValues = random.sample(range(1, max(arr)), k)
meanValues.sort()
clusters = {}
for i in range(k):
    clusters[i+1] = []
for i in arr:
    clusters[nearestCluster(i, meanValues)].append(i)

iterations = 1
while True:
    printIter(iterations, clusters, k, meanValues)
    iterations += 1

    meanValues = newMean(clusters)
    newClusters = {}
    for i in range(k):
        newClusters[i + 1] = []
    for i in arr:
        newClusters[nearestCluster(i, meanValues)].append(i)
    if clusters == newClusters:
        break
    clusters = newClusters

# testcase -> 1 2 5 6 7 8 9 10 11 12 12 15 17 20 23
# 2 4 10 12 3 20 30 11 25
# 5 9 11 13 2 20 18 25 50 30 8 32 24 27 17
