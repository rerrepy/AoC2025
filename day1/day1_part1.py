dial=50
code=0
with open ('day1.txt', 'r') as file:
    for line in file:
        rot=int(line.strip()[1:])
        
        if line[0] == 'L':
            dial -= rot
        else:
            dial += rot
        if dial % 100 == 0:
            code += 1
print(code)