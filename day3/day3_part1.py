joltage = 0
with open ('day3.txt', 'r') as file:
    for line in file:
        bank = line.strip()
        first_digit = max(bank[:len(bank)-1])
        index_first_digit = bank.find(first_digit)
        second_digit = max(bank[index_first_digit+1:])
        joltage += int(first_digit + second_digit)

print(joltage)