divisor = int(input())
bound = int(input())

max_number = 0

for number in range(1 , bound + 1):
    if number % divisor == 0 and number <= bound:
        max_number = number
    else:
        continue
print(max_number)
