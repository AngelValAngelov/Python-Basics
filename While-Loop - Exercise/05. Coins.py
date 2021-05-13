import math

receive = float(input())
receive = math.floor(receive * 100)
coins_count = 0
money_left = receive

while money_left > 0:
    if money_left >= 200:
        money_left -= 200
        coins_count += 1
    elif money_left >= 100:
        money_left -= 100
        coins_count += 1
    elif money_left >= 50:
        money_left -= 50
        coins_count += 1
    elif money_left >= 20:
        money_left -= 20
        coins_count += 1
    elif money_left >= 10:
        money_left -= 10
        coins_count += 1
    elif money_left >= 5:
        money_left -= 5
        coins_count += 1
    elif money_left >= 2:
        money_left -= 2
        coins_count += 1
    elif money_left >= 1:
        money_left -= 1
        coins_count += 1

print(coins_count)

