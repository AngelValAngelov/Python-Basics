import sys

n = int(input())
max_number = -sys.maxsize

while n > 0:
    number = int(input())
    if number > max_number:
        max_number = number
    n -= 1

print(max_number)