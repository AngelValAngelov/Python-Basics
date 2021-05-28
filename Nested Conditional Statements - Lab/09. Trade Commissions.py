city = input()
number = float(input())
percent = 0
result = 0

if city == "Sofia" and 0 <= number <= 500:
    result = number * 0.05
elif city == "Sofia" and 500 < number <= 1000:
    result = number * 0.07
elif city == "Sofia" and 1000 < number <= 10000:
    result = number * 0.08
elif city == "Sofia" and number > 10000:
    result = number * 0.12
if city == "Varna" and 0 <= number <= 500:
    result = number * 0.045
elif city == "Varna" and 500 < number <= 1000:
    result = number * 0.075
elif city == "Varna" and 1000 < number <= 10000:
    result = number * 0.10
elif city == "Varna" and number > 10000:
    result = number * 0.13
if city == "Plovdiv" and 0 <= number <= 500:
    result = number * 0.055
elif city == "Plovdiv" and 500 < number <= 1000:
    result = number * 0.08
elif city == "Plovdiv" and 1000 < number <= 10000:
    result = number * 0.12
elif city == "Plovdiv" and number > 10000:
    result = number * 0.145

if result:
    print(f"{result:.2f}")
else:
    print("error")