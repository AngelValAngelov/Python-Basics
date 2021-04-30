name = input()
mark = float(input())

count = 12
result = 0

while count > 0:
    if mark >= 4:
        result += mark
        count -= 1
        if count > 0:
            mark = float(input())
        else:
            break
    else:
        mark = float(input())

print(f"{name} graduated. Average grade: {result / 12:.2f}")