import math

year = input()
p = int(input())
h = int(input())
days = 0

if year == "normal":
    days = ((48 - h) * 3/4) + h + (p * 2/3)
else:
    days = ((48 - h) * 0.75 + h + (p * 2/3)) * 1.15

print(math.floor(days))