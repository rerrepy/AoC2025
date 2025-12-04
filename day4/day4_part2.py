def nb_count(ix_x, ix_y, paper):
    nb_paper = 0
    height = len(paper)
    width = len(paper[0])
    for y in range (-1, 2):
        for x in range (-1, 2):
            if 0 <= ix_y + y < height and 0 <= ix_x + x < width:
                if x == 0 and y == 0:
                    continue
                if paper[ix_y + y][ix_x + x] == '@':
                    nb_paper += 1
    return nb_paper
    
paper_arr = []
sum_paper = 0
prev_sum_paper = -1

with open('day4.txt', 'r') as file:
    for line in file.readlines():
        paper_arr.append(list(line.strip()))

while sum_paper != prev_sum_paper:
    prev_sum_paper = sum_paper
    for y in range(0, len(paper_arr)):
        for x in range (0, len(paper_arr[0])):
            if paper_arr[y][x] == '@': 
                if nb_count(x, y, paper_arr) < 4:
                    paper_arr[y][x] = 'x'
                    sum_paper += 1

print(sum_paper)