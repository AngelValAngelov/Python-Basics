interval_begin = int(input())
interval_end = int(input())
magic_number = int(input())

combination = 0
summ = None
for number in range(interval_begin, interval_end + 1):
    if magic_number == summ:
        break
    for num in range(interval_begin, interval_end + 1):
        combination += 1
        summ = number + num
        if magic_number == summ:
            print(f"Combination N:{combination} ({number} + {num} = {magic_number})")
            break
if magic_number != summ:
    print(f"{combination} combinations - neither equals {magic_number}")