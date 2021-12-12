import numpy as np
data = []

def increase(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            array[i][j] += 1

with open("input", "r") as file:
    for line in file:
        data.append(list(map(int, line[:-1])))

flashed = np.full_like(data, 0)

end = False
steps = 0
while not end:
    steps += 1
    flashed = np.full_like(data, 0)
    found = True
    for d in data:
        print(d)
    print(steps)
    increase(data)
    h = 0
    flashes = 0
    while found:
        h += 1
        found = False
        for i in range(10):
            for j in range(10):
                if data[i][j] > 9:
                    flashes += 1
                    data[i][j] = 0
                    flashed[i][j] = 1
                    found = True
                    for x in range(i - 1, i + 2):
                        for y in range(j - 1, j + 2):
                            if x >= 0 and x < 10:
                                if y >= 0 and y < 10:
                                    if flashed[x][y] == 0:
                                        data[x][y] += 1
    if flashes == 100:
        end = True

print(steps)
