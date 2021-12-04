import numpy as np
import sys

LEN = 5
def is_bingo(matrix):
    for i in range(LEN):
        count = 0
        for j in range(LEN):
            count += matrix[i][j][1]
        if count == LEN:
            return True

    for i in range(LEN):
        count = 0
        for j in range(LEN):
            count += matrix[j][i][1]
        if count == LEN:
            return True

    return False

def mark_matrix(matrix, num):
    for i in range(LEN):
        for j in range(LEN):
            if matrix[i][j][0] == num:
                matrix[i][j] = (matrix[i][j][0], 1)
            

def sum_unmarked(matrix):
    sm = 0
    for i in range(LEN):
        for j in range(LEN):
            if matrix[i][j][1] == 0:
                sm += matrix[i][j][0]

    return sm

lines = []
with open ("input", "r") as file:
    for line in file:
        lines.append(line)

nums = list(map(int, lines[0].split(',')))
index = 1
matrices = []
while True:
    index += 1
    if index > len(lines) - 1:
        break

    matrix = []
    for i in range(5):
        line = list(map(int, lines[index].split()))
        line = [(x, 0) for x in line]
        matrix.append(line)
        index += 1

    matrices.append(matrix)

for num in nums:
    ln = len(matrices)
    for index, matrix in enumerate(matrices):
        mark_matrix(matrix, num)
        if is_bingo(matrix):
            matrices.pop(index)
    if len(matrices) == 1:
        print(sum_unmarked(matrix) * num)
        break
