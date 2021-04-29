import sys

n = int(input())
min_number = sys.maxsize

while n > 0:
    number = int(input())
    if number < min_number:
        min_number = number
    n -= 1

print(min_number)