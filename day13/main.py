import numpy as np
data = []
folds = []
max_x = 0
max_y = 0 
with open("input", "r") as file:
    for line in file:
        if line == '\n':
            continue
        line = line[:-1]
        if line[0] == 'f':
            folds.append([line.split('=')[0][-1], int(line.split('=')[-1])])
        else:
            y, x = map(int, line.split(','))
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            data.append([x, y])

print(max_x)
print(max_y)
max_x += 1
max_y += 1

matrix = np.zeros((max_x, max_y))
for d in data:
    matrix[d[0]][d[1]] = 1

for fold in folds[:1]:
    if fold[0] == 'x':
        for i in range(max_x):
            move = 1
            for j in range(fold[1] + 1, max_y):
                if matrix[i][j] == 1:
                    new_y = fold[1] - move
                    print(j, new_y)
                    matrix[i][new_y] = 1
                move += 1

        max_y = fold[1]
        matrix = matrix[::, :fold[1]].copy()

    else:
        move = 0
        for i in range(fold[1] + 1, max_x):
            move += 1
            for j in range(max_y):
                if matrix[i][j] == 1:
                    new_x = fold[1] - move
                    matrix[new_x][j] = 1

        matrix = matrix[:fold[1], ::].copy()
        max_x = fold[1]

    print(matrix)

print(np.sum(matrix))

