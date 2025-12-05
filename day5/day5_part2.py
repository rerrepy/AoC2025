
id_intervals = []

with open('day5.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        if line == '':
            break
        lower, upper = line.split('-')
        id_intervals.append([int(lower), int(upper)])


id_intervals.sort(key=lambda x: x[0])


#id_intervals = [[1, 2], [1, 3], [1,5], [10,15]]
# Merge intervals
# We should merge two intervals IF
# first interval upper limit >= second interval lesser limit
while True:
    merged_happened = False
    
    for i in range(len(id_intervals) - 1):
        current_interval = id_intervals[i]
        next_interval = id_intervals[i+1]
        
        current_upper = current_interval[1]
        next_lower = next_interval[0]
        next_upper = next_interval[1]
        
        if current_upper >= next_lower:
            # Merge the highest upper limit
            id_intervals[i][1] = max(current_upper, next_upper)
            # Remove the next interval so no double processing
            del id_intervals[i+1]

            merged_happened = True
            # Restart from beginning
            break 
    # If we never merged in the entire list, bail
    if not merged_happened:
        break


sum_ids = 0
for i in id_intervals:
    sum_ids += i[1] - i[0] + 1
    
print(sum_ids)
    
