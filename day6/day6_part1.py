import operator
from functools import reduce # distinct import needed

problems = []
with open('day6.txt', 'r') as file:
    for line in file.readlines():
        problems.append(line.split())
operators_list = problems[-1]

tot = 0
for i in range(len(problems[0])):
    current_operator = operators_list[i]
    if current_operator == '+':
        math_operator = operator.add
    else:
        math_operator = operator.mul
    current_digits = []
    for y in range(len(problems) - 1):
        current_digits.append(int(problems[y][i]))
    current_tot = reduce(math_operator, current_digits)
    tot += current_tot

print(tot)