joltage = 0

with open ('day3.txt', 'r') as file:
    for line in file:
        index_highest_digit = -1
        current_joltage = ""
        bank = line.strip()
        for i in range(0, 12):
            # The index of the first occurence of the latest highest digit. We must scan strictly after this index.
            offset = index_highest_digit+1
            # How much space we must leave on the right side to fit all remaining digits
            leave_space = len(bank)-(11 - i)
            highest_digit = max(bank[offset:leave_space])
            # Add offset because we do find on a subset of the digits, specifically 'offset' number of digits ahead.
            index_highest_digit = bank[offset:leave_space].find(highest_digit) + offset
            current_joltage += highest_digit
        joltage += int(current_joltage)

print(joltage)