with open("input", "r") as file:
    data = []
    for index, line in enumerate(file):
        part = line.split('|')[1]
        data.append(part)

count = 0
for i in range(len(data)):
    data[i] = data[i].split()
    for word in data[i]:
        if len(word) in [2, 3, 4, 7]:
            count += 1

print(count)
