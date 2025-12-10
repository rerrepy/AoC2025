tiles = []

with open('day9.txt', 'r') as file:
    for line in file.readlines():
        tiles.append([int(n) for n in line.strip().split(',')])
      
def calc_area(p1, p2):
    p1_x = p1[0]
    p1_y = p1[1]
    p2_x = p2[0]
    p2_y = p2[1]
    
    w = abs(p1_x - p2_x) + 1
    h = abs(p1_y - p2_y) + 1
    return w * h

greatest = 0
for p1 in tiles:
    for p2 in tiles:
        curr_area = calc_area(p1, p2)
        if curr_area > greatest:
            greatest = curr_area

print(greatest)
        
