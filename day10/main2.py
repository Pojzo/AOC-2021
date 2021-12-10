data = []
with open("input", "r") as file:
    for line in file:
        cur_line = line[:-1]
        data.append(cur_line)

dic = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {'(' : 1, '[': 2, '{': 3, '<': 4}

correct_lines = []
for line in data:
    stack = []
    correct = True
    for item in line:
        if item in dic:
            stack.append(item)
        else:
            if item == dic[stack[-1]]:
                stack.pop(-1)
            else:
                correct = False
                break

    if correct is True:
        correct_lines.append(line)


scores = []

stacks = []
for line in correct_lines:
    stack = []
    for item in line:
        if item in dic:
            stack.append(item)
        else:
            if item == dic[stack[-1]]:
                stack.pop(-1)
     
    stacks.append(reversed(stack)) 

scores = []
for stack in stacks:
    cur_score = 0
    for item in stack:
        print(item, cur_score, end = " ")
        cur_score *= 5
        cur_score += points[item]

    print()
    scores.append(cur_score)

scores = sorted(scores)
print(scores[len(scores) // 2])
