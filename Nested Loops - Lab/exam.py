guest_count = int(input())
gift_count = int(input())

a = 0
b = 0
v = 0
g = 0

for guest in range(gift_count):
    categorry = input()
    if categorry == "A":
        a += 1
    elif categorry == "B":
        b += 1
    elif categorry == "V":
        v += 1
    elif categorry == "G":
        g += 1

percent_a = (a / gift_count) * 100
percent_b = (b / gift_count) * 100
percent_v = (v / gift_count) * 100
percent_g = (g / gift_count) * 100
percent_gest_give_gift = (gift_count / guest_count) * 100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{percent_gest_give_gift:.2f}%")

