n = int(input())

capacity_left = 0
for number in range(n):
    quantity = int(input())
    if capacity_left + quantity > 255:
        print("Insufficient capacity!")
        continue
    else:
        capacity_left += quantity

print(f"{capacity_left}")
