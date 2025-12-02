def sum_invalid(i):
    for div in range (2, len(i) + 1):
        if len(i) % div == 0:
            # If div is 3 and string is 121212 we get 12
            sub_id = i[:len(i) // div]
            reconstructed = sub_id * div
            if reconstructed == i:
                return int(i)
    return 0

invalid_id_sum=0
with open ('day2.txt', 'r') as file:
    for line in file:
        id_ranges = line.split(',')
        for id_range in id_ranges:
            start, end = map(int, id_range.split('-'))
            for i in range (start, end + 1):
                invalid_id_sum += sum_invalid(str(i))

print(invalid_id_sum)
                    
                    
                
