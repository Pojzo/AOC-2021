import numpy as np
import heapq
from collections import defaultdict
import sys

# X = 100
# Y = 100

matrix = []
with open("input", "r") as file:
    for line in file:
        matrix.append(list(map(int, line[:-1])))

X = len(matrix)
Y = len(matrix[0])

new_matrix = np.zeros((X * 5, Y * 5))
for i in range(5):
    for j in range(5):
        for x in range(X):
            for y in range(Y):
                if i == 0 and j == 0:
                    new_matrix[x][y] = (matrix[x][y])
                else:
                    if i == 0:
                        new_matrix[x][j * Y + y] = new_matrix[x][(j - 1) * Y + y] + 1
                        if new_matrix[x][j * Y + y] == 10:
                            new_matrix[x][j * Y + y]  = 1

                    elif j == 0:
                        new_matrix[i * X + x][y] = new_matrix[(i - 1) * X + x][y] + 1
                        if new_matrix[i * X + x][y] == 10:
                            new_matrix[i * X + x][y] = 1
                    else:
                        new_matrix[i * X + x][j * Y + y] = new_matrix[(i - 1) * X + x][j * Y + y] + 1
                        if new_matrix[i * X + x][j * Y + y] == 10:
                            new_matrix[i * X + x][j * Y + y] = 1


# cost, row, column
queue = [(0, 0, 0)]
heapq.heapify(queue)
cost = dict()
visited = set()
X = len(new_matrix)
Y = len(new_matrix[0])
# now I understand Djikstras algorithm
# https://github.com/womogenes/AoC-2021-Solutions/blob/main/day_15/day_15_p1.py
# https://www.youtube.com/watch?v=DYUfkN9D88s
while len(queue):
    c, row, col = heapq.heappop(queue)
    if (row, col) in visited:
        continue
    visited.add((row, col))
    cost[(row, col)] = c
    
    for row_change, col_change in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        new_r = row + row_change
        new_c = col + col_change
        if new_r < 0 or new_r > X - 1:
            continue
        if new_c < 0 or new_c > Y - 1:
            continue

        heapq.heappush(queue, (c + new_matrix[new_r][new_c], new_r, new_c))

print(cost[(X-1, Y-1)])
