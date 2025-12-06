import operator
from functools import reduce # distinct import needed

problems = []
with open('day6.txt', 'r') as file:
    for line in file:
        problems.append(line.strip('\n'))

operators = problems[-1].split()
del problems[-1]

def is_blank_column(arr, x):
    for y in range(len(arr)):
        if arr[y][x] != ' ':
            return False
    return True

int_list = []
total_ints = []
for x in range(len(problems[0])):
    if not is_blank_column(problems, x):
        current_int = ""
        for y in range(len(problems)):
            current_item = problems[y][x]
            if current_item != ' ':
                current_int += current_item
        int_list.append(int(current_int))
    else:
        total_ints.append(int_list)
        int_list = []
total_ints.append(int_list)

current_tot = 0
for i, current_digits in enumerate(total_ints):
    current_operator = operators[i]
    if current_operator == '+':
        math_operator = operator.add
    else:
        math_operator = operator.mul
    
    current_tot += reduce(math_operator, current_digits)    

print(current_tot)


