n = int(input())

sum_even = 0
sum_odd = 0

for number in range(n):
    num = int(input())
    if number % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

if sum_even == sum_odd:
    print(f"Yes\nSum = {sum_odd}")
else:
    diff = abs(sum_odd - sum_even)
    print(f"No\nDiff = {diff}")