import math
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    z: int
    group: int = 0
      

points = []
with open ('day8.txt', 'r') as file:
    current_point = []
    for line in file:
        coords = [int(n) for n in line.strip().split(',')]
        points.append(Point(*coords))


def euclidean_distance(p1, p2):
    return math.sqrt(
        math.pow(p1.x - p2.x, 2) + 
        math.pow(p1.y - p2.y, 2) +
        math.pow(p1.z - p2.z, 2)
    )

distances = []

for c, p1 in enumerate(points):
    for n, p2 in enumerate(points):
        if c == n:
            continue
        distance = euclidean_distance(p1, p2)
        distances.append((distance, p1, p2))
        

#for i in distances:
    #print(i)

distances.sort(key=lambda x: x[0])


#distances[0][1].group = 1
#print(distances[0][1])
#exit()

curr_group_id = 1

for d_p in distances:
    p1 = d_p[1]
    p2 = d_p[2]
    if p1.group == p2.group and p1.group != 0 and p2.group != 0:
        continue
    elif p1.group > 0 and p2.group > 0:
        #input("BUGG")
        continue
    elif p1.group > 0:
        p2.group = p1.group
    elif p2.group > 0:
        p1.group = p2.group
    else:
        p1.group = curr_group_id
        p2.group = curr_group_id
        curr_group_id += 1
    
        

for p in distances:
    print(p[1], p[2])

count_groups = []
current_group = 1
current_count = 0

while current_group < 100:
    for p in points:
        if p.group == current_group:
            current_count += 1
    count_groups.append((current_group, current_count))
    current_group += 1
    current_count = 0


count_groups.sort(key=lambda x: x[1], reverse=True)


print(count_groups)