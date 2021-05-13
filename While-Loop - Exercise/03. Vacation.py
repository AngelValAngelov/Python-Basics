money_needed = float(input())
money = float(input())
action = input()
money_save_action = int(input())
days = 0
spend_count = 0

while money < money_needed or money > 0:
    if action == "save":
        days += 1
        money = money + money_save_action
        if money < money_needed:
            action = input()
            money_save_action = int(input())
        else:
            print(f"You saved the money for {days} days.")
            break
    else:
        spend_count += 1
        if spend_count >= 5:
            break
        else:
            if spend_count >= 5:
                days += 1
                money = money - money_save_action
                action = input()
                money_save_action = int(input())
            if money < 0:
                money = 0


if money_needed > money and spend_count < 5:
    print(f"You can't save the money.\n{days}")
else:
    print(f"You can't save the money.\n{spend_count}")