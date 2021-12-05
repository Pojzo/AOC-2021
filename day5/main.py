import numpy as np

size_x = 990
size_y = 990

data = []

def count_overlap(matrix):
    sm = 0
    for i in range(size_x):
        for j in range(size_y):
            if matrix[i][j] >= 2:
                sm += 1
    return sm

with open("input", "r") as file:
    for line in file:
        data.append(line)

matrix = np.zeros((size_x, size_y))
max_x = 0
max_y = 0

for line in data:
    separation = line.split('->')

    coord1 = separation[0].split(',')
    coord2 = separation[1].split(',')

    first_x = int(coord1[0])
    first_y = int(coord1[1])

    second_x = int(coord2[0])
    second_y = int(coord2[1])

    if first_y == second_y:
        min_x = min(first_x, second_x)
        max_x = max(first_x, second_x)
        for i in range(min_x, max_x + 1):
            matrix[first_y][i] += 1

    if first_x == second_x:
        min_y = min(first_y, second_y)
        max_y = max(first_y, second_y)
        for j in range(min_y, max_y + 1):
            matrix[j][first_x] += 1

print(count_overlap(matrix))
