dial = 50  # This will grow infinitely (e.g. 1050, -200, etc)
code = 0

with open('day1.txt', 'r') as file:
    for line in file:
        rot=int(line.strip()[1:])
        
        if line[0] == 'L':
            new_dial = dial - rot
            code += ((dial - 1) // 100) - ((new_dial - 1) // 100)
            dial = new_dial
        else:
            new_dial = dial + rot
            code += (new_dial // 100) - (dial // 100)
            dial = new_dial
            

print(code)