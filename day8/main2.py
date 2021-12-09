import itertools

# Probably the ugliest code I've ever written
# Bruteforce solution

output = []
data = []
with open("input", "r") as file:
    for index, line in enumerate(file):
        cur_data = line.split()
        cur_data.remove('|')
        data.append(cur_data)
        output.append(line.split('|')[1].split())


lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 6, 2, 5, 5, 4, 5, 6, 3, 7, 6
nums_list =  ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

nums = set(nums_list)

all_permutations = [list(zip(x, lst)) for x in itertools.permutations(lst, len(lst))]

global_sum = 0
all_good = True
index = 0
for i in range(len(data)):
    for permutation in all_permutations:
        cur_dic = {x[0]: x[1] for x in permutation} 
        new_array = []
        for x in data[i]:
            new_string = ""
            for letter in x:
                new_string += cur_dic[letter]
            new_array.append(new_string)

        all_good = True
        for item in new_array:
            if not "".join(sorted(item)) in nums: 
                all_good = False
                break

        if all_good:
            index = i
            break

    if all_good:
        sm = 0
        new_line = []
        for word in output[i]:
            new_word = ""
            for letter in word:
                new_word += cur_dic[letter]
            new_line.append("".join(sorted(new_word)))
        numbers = []
        for word in new_line:
            numbers.append(str(nums_list.index(word)))
        str_num = "".join(numbers)
        global_sum += int(str_num)

print("RESULT: ", global_sum)

