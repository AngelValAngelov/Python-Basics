n = int(input())
summ = 0
max_num = 0

for number in range(n):
    num = int(input())
    summ += num
    if num > max_num:
        max_num = num
if summ - max_num == max_num:
        print(f"Yes\nSum = {max_num}")
else:
    diff = abs(max_num - (summ - max_num))
    print(f"No\nDiff = {diff}")
