n = int(input())
sum_left = 0
sum_right = 0

for num in range(n):
    number = int(input())
    sum_left += number

for num in range(n):
    number = int(input())
    sum_right += number

if sum_right == sum_left:
    print(f"Yes, sum = {sum_right}")
else:
    sums = abs(sum_right - sum_left)
    print(f"No, diff = {sums}")