fruit = input()
day_week = input()
quantity = float(input())
money = 0


if (day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday"
    or day_week == "Thursday" or day_week == "Friday") and fruit == "banana":
    money = 2.5 * quantity
elif (day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday"
    or day_week == "Thursday" or day_week == "Friday") and fruit == "apple":
    money = 1.20 * quantity
elif (day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday"
    or day_week == "Thursday" or day_week == "Friday") and fruit == "orange":
    money = 0.85 * quantity
elif (day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday"
    or day_week == "Thursday" or day_week == "Friday") and fruit == "grapeefruit":
    money = 1.45 * quantity
elif (day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday"
    or day_week == "Thursday" or day_week == "Friday") and fruit == "kiwi":
    money = 2.70 * quantity
elif (day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday"
    or day_week == "Thursday" or day_week == "Friday") and fruit == "pineapple":
    money = 5.50 * quantity
elif (day_week == "Monday" or day_week == "Tuesday" or day_week == "Wednesday"
    or day_week == "Thursday" or day_week == "Friday") and fruit == "grapes":
    money = 3.85 * quantity
elif (day_week == "Saturday" or day_week == "Sunday") and fruit == "banana":
    money = 2.70 * quantity
elif (day_week == "Saturday" or day_week == "Sunday") and fruit == "apple":
    money = 1.25 * quantity
elif (day_week == "Saturday" or day_week == "Sunday") and fruit == "orange":
    money = 0.90 * quantity
elif (day_week == "Saturday" or day_week == "Sunday") and fruit == "grapefruit":
    money = 1.60 * quantity
elif (day_week == "Saturday" or day_week == "Sunday") and fruit == "kiwi":
    money = 3.00 * quantity
elif (day_week == "Saturday" or day_week == "Sunday") and fruit == "pineapple":
    money = 5.60 * quantity
elif (day_week == "Saturday" or day_week == "Sunday") and fruit == "grapes":
    money = 4.20 * quantity

if money:
    print(f"{money:.2f}")
else:
    print("error")