import numpy as np
import sys

# this guy helped me a lot
# https://www.youtube.com/watch?v=lBRtnuxg-gU

X = 100
Y = 100

X = 5
Y = 5

matrix = []
with open("mysample", "r") as file:
    for line in file:
        matrix.append(list(map(int, line[:-1])))

def min_cost(matrix):
    dist = np.zeros((X + 1, Y + 1))
    sm = -matrix[0][0]
    for i in range(X):
        dist[i][0] = sm + matrix[i][0]
        sm = dist[i][0]

    sm = -matrix[0][0]
    for j in range(Y):
        dist[0][j] = sm + matrix[0][j]
        sm = dist[0][j]

    dist[0][0] = 0
    for j in range(1, Y):
        for i in range(1, X):
            dist[i][j] = matrix[i][j] + min(dist[i - 1][j], dist[i][j - 1])
        
    return dist

dist_matrix = min_cost(matrix)
min_dist = int(dist_matrix[-1][-1])

print(min_dist)
