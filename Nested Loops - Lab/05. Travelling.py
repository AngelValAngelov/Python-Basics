country = input()

while country != "End":
    all_money = 0
    money_needed = float(input())
    while all_money < money_needed:
        money = float(input())
        all_money += money
    if all_money >= money_needed:
        print(f"Going to {country}!")
        all_money = 0
        country = input()





