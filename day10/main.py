data = []
with open("input", "r") as file:
    for line in file:
        cur_line = line[:-1]
        data.append(cur_line)

dic = {'(': ')', '[': ']', '{': '}', '<': '>'}
points = {')' : 3, ']': 57, '}': 1197, '>': 25137}

score = 0
for line in data:
    stack = []
    for item in line:
        if item in dic:
            stack.append(item)
        else:
            if item == dic[stack[-1]]:
                stack.pop(-1)
            else:
                score += points[item]
                break
     
print(score)
