import numpy as np
import sys
sys.setrecursionlimit(1000)

# lol funguje to xdd 

def count(arr, visited, sm, x, y):
    if x < 0 or x > len(arr) - 1:
        return 0
    if y < 0  or y > len(arr[0]) - 1:
        return 0
    
    if visited[x][y] == 1:
        return 0

    if arr[x][y] == 9:
        return 0

    sm = 1
    visited[x][y] = 1
    
    return sm + count(arr, visited, sm, x - 1, y) + count(arr, visited, sm, x + 1, y) + count(arr, visited, sm, x, y -
            1) + count(arr, visited, sm, x, y + 1) 

data = []
with open("input", "r") as file:
    for line in file:
        line = [int(x) for x in line[:-1]]
        data.append(line)

visited = np.full_like(data, 0)
islands = []
for x in range(1, len(data) - 1):
    for y in range(1, len(data[0]) - 1):
        if data[x][y] != 9 and visited[x][y] == 0:
            islands.append(count(data, visited, 0, x, y))

islands = sorted(islands)
print(islands)
print(islands[-1] * islands[-2] * islands[-3])
