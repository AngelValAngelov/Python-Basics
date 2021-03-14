type = input()
r = int(input())
c = int(input())

max_seets = r * c
result = 0

if type == "Premiere":
    result = max_seets * 12
elif type == "Normal":
    result = max_seets * 7.50
else:
    result = max_seets * 5

print(f"{result:.2f} leva")