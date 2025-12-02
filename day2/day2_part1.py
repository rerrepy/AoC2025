def is_invalid(i):
    half_i_len = len(i) // 2
    return i[:half_i_len] == i[half_i_len:]

invalid_id_sum=0
with open ('day2.txt', 'r') as file:
    for line in file:
        id_ranges = line.split(',')
        for id_range in id_ranges:
            start, end = map(int, id_range.split('-'))
            for i in range (start, end + 1):
                if is_invalid(str(i)):
                    invalid_id_sum += i

print(invalid_id_sum)
                    
                    
                
