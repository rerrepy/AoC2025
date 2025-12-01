dial=50
prev_dial=50
code=0
with open ('day1.txt', 'r') as file:
    for line in file:
        rotation=int(line.strip()[1:])
        if line[0] == 'L':
            dial -= rotation
        else:
            dial += rotation
        if dial % 100 == 0:
            code += 1
print(code)