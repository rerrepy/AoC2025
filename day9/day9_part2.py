tiles = []

with open('day9.txt', 'r') as file:
    for line in file.readlines():
        tiles.append([int(n) for n in line.strip().split(',')])




smallest_x = tiles[0][0]
smallest_y = tiles[0][1]
greatest_x = tiles[0][0]
greatest_y = tiles[0][1]

for tile in tiles:
    t_x = tile[0]
    t_y = tile[1]
    if t_x > greatest_x:
        greatest_x = t_x
    if t_y > greatest_y:
        greatest_y = t_y
    if t_x < smallest_x:
        smallest_x = t_x
    if t_y < smallest_y:
        smallest_y = t_y

#print(smallest_y, smallest_x, greatest_y, greatest_x)
    
rows = greatest_x - smallest_x + 1
cols = greatest_y - smallest_y + 1
print(rows, cols)
score_board = [['.' for _ in range(cols)] for _ in range(rows)]
for row in score_board:
    print(row)
offset_x = smallest_x
offset_y = smallest_y

for tile in tiles:
    t_x = tile[0]
    t_y = tile[1]
    print(offset_y - t_y, offset_x - t_x)
    score_board[offset_y - t_y][offset_x - t_x] = '#'

for row in score_board:
    print(row)
    
exit()


for tile in tiles:
    t_x = tile[0]
    t_y = tile[1]
print(tiles)
exit()


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
        
