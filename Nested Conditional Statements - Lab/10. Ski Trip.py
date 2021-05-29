days = int(input()) - 1
flat = input()
mark = input()
money = 0
if flat == "room for one person" and days < 10:
    money = days * 18
elif flat == "room for one person" and 10 <= days <= 15:
    money = days * 18
elif flat == "room for one person" and days > 15:
    money = days * 18
elif flat == "apartment" and days < 10:
    money = (days * 25) * 0.70
elif flat == "apartment" and 10 <= days <= 15:
    money = (days * 25) * 0.65
elif flat == "apartment" and days > 15:
    money = (days * 25) * 0.50
elif flat == "president apartment" and days < 10:
    money = (days * 35) * 0.90
elif flat == "president apartment" and 10 <= days <= 15:
    money = (days * 35) * 0.85
elif flat == "president apartment" and days > 15:
    money = (days * 35) * 0.80

if mark == "positive":
    money *= 1.25
else:
    money *= 0.90

print(f"{money:.2f}")