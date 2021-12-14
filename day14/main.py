from collections import Counter

data = []
with open("sample", "r") as file:
    for line in file:
        if not line == '\n':
            data.append(line[:-1])

template = data[0]
instructions = []
dic = dict()
for d in data[1:]:
    instructions.append(d.split(' -> '))
    dic[instructions[-1][0]] = instructions[-1][1]
     

steps = 3
for step in range(steps):
    print(step)
    index = 0
    print(template)
    while index < len(template) - 1:
        cur = template[index : index + 2]
        if cur in dic:
            template = template[:index + 1] + dic[cur] + template[index + 1:]

        index += 2 

counter = Counter(template)
values = sorted(counter.values())
print(values[-1] - values[0])
