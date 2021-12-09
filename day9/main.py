data = []
with open("input", "r") as file:
    for line in file:
        line = [x for x in line[:-1]]
        line.insert(0, 10)
        line.append(10)
        data.append(line)

data.insert(0, [10 for _ in range(len(data[0]))])
data.append([10 for _ in range(len(data[0]))])

count = 0
low_points = []
for i in range(1, len(data) - 1):
    for j in range(1, len(data[0]) - 1):
        current = 0
        # print(data[i][j], data[i][j - 1], data[i][j + 1], data[i - 1][j], data[i + 1][j])
        if int(data[i][j - 1]) > int(data[i][j]):
            current += 1
        if int(data[i][j + 1]) > int(data[i][j]):
            current += 1
        if int(data[i - 1][j]) > int(data[i][j]):
            current += 1
        if int(data[i + 1][j]) > int(data[i][j]):
            current += 1
        
        if current == 4:
            low_points.append(data[i][j])
            count += 1

print(count)
print(sum(list(map(int, low_points))) + count)
