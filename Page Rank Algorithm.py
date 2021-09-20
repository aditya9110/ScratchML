n = int(input('Enter numbers of vertices: '))

graph = []
print('Enter the adjacency matrix for the graph')
for i in range(n):
    graph.append(list(map(int, input().split())))

iterations = 1
d = 0.85
currPR = [1] * n
prevPR = []

while True:
    for j in range(n):
        innerRes = 0.0
        for k in range(n):
            if graph[k][j]:
                innerRes += (currPR[k] / sum(graph[k]))
        currPR[j] = 1 - d + (d * innerRes)
    if currPR == prevPR:
        break
    prevPR = list(currPR)
    print('Iteration ' + str(iterations) + ': ')
    iterations += 1
    print(currPR)

print('Iteration ' + str(iterations) + ': ')
print(currPR)
