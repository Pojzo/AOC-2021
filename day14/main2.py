from collections import Counter
# ugly code lmao xd

data = []
with open("input", "r") as file:
    for line in file:
        if not line == '\n':
            data.append(line[:-1])

template = data[0]
instructions = []
dic = dict()
dic_count = dict()
unique = set()
for d in data[1:]:
    instructions.append(d.split(' -> '))
    dic[instructions[-1][0]] = instructions[-1][1]
    dic_count[instructions[-1][0]] = 0
     
for pair in instructions:
    unique.add(pair[0][0])
    unique.add(pair[0][1])
    unique.add(pair[1][0])

dic_letters = {x: 0 for x in unique}
for i in range(len(template) - 1):
    dic_count[template[i:i+2]] += 1
    dic_letters[template[i]] += 1

dic_letters[template[-1]] += 1

steps = 40
for step in range(steps):
    dummy_dic = dict(dic_count)
    for item in dummy_dic:
        new_letter = dic[item]
        dic_letters[new_letter] += dummy_dic[item]
        dic_count[item] -= dummy_dic[item]

        first_pair = item[0] + new_letter
        second_pair = new_letter + item[1]

        dic_count[first_pair] += dummy_dic[item]
        dic_count[second_pair] += dummy_dic[item]

values = sorted(dic_letters.values())
print(values[-1] - values[0])
