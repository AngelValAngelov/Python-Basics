age = int(input())
washing_mashine_price = float(input())
toy_price = int(input())
toy_counter = 0
money = 0
money_counter = 0
bro_stealer = 1

for number in range(1, age + 1, 2):
    toy_counter += 1

for number in range(2, age + 1, 2):
    money = money + 10 + money_counter
    money_counter += 10
    money = money - bro_stealer

toy_money = toy_counter * toy_price
money += toy_money

if washing_mashine_price <= money:
    money = abs(money - washing_mashine_price)
    print(f"Yes! {money:.2f}")
else:
    money = abs(washing_mashine_price - money)
    print(f"No! {money:.2f}")