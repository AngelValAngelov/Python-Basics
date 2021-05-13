money_needed = float(input())
money = float(input())
action = input()
money_spended_save = float(input())
spent = 0
day = 0

while money < money_needed:
    if action == "save":
        spent = 0
        day += 1
        money += money_spended_save
        if money >= money_needed:
            break
        else:
            action = input()
            money_spended_save = float(input())
    else:
        spent += 1
        day += 1
        money -= money_spended_save
        if money < 0:
            money = 0
        if spent > 4:
            break
        else:
            action = input()
            money_spended_save = float(input())

if money >= money_needed:
    print(f"You saved the money for {day} days.")
else:
    print(f"You can't save the money.\n{day}")

