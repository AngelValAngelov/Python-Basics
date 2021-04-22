import math

party_size = int(input())
days = int(input())

coins_gained = 0
stuff = party_size

for day in range(1, days + 1):
    if day % 10 == 0:
        stuff -= 2
    if day % 15 == 0:
        stuff += 5
    coins_gained += 50 - (2 * stuff)
    if day % 3 == 0:
        coins_gained -= (3 * stuff)
    if day % 5 == 0:
        coins_gained += (20 * stuff)
    if day % 5 == 0 and day % 3 == 0:
        coins_gained -= (2 * stuff)

print(f"{stuff} companions received {math.floor(coins_gained / stuff)} coins each.")