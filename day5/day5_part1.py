
def is_in_any_interval(intervals, check_id):
    check_id = int(check_id) 
    for i in intervals:
        separated_intervals = i.split('-')
        lower_interval = int(separated_intervals[0])
        upper_interval = int(separated_intervals[1])
        if lower_interval <= check_id <= upper_interval:
            return True
    return False

id_intervals = []
ids = []
found_empty = False

with open('day5.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        if line == '':
            found_empty = True
            continue
        if found_empty == False:
            id_intervals.append(line)
        else:
            ids.append(line)

sum_fresh = 0
for id in ids:
    if is_in_any_interval(id_intervals, id):
        sum_fresh += 1

print(sum_fresh)