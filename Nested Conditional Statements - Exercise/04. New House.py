flowers_kind = input()
flowers_count = int(input())
budget = int(input())

money = 0

if flowers_kind == "Roses" and flowers_count > 80:
    money = (flowers_count * 5) * 0.90
elif flowers_kind == "Roses" and flowers_count <= 80:
    money = flowers_count * 5
elif flowers_kind == "Dahlias" and flowers_count > 90:
    money = (flowers_count * 3.80) * 0.85
elif flowers_kind == "Dahlias" and flowers_count <= 90:
    money = flowers_count * 3.80
elif flowers_kind == "Tulips" and flowers_count > 80:
    money = (flowers_count * 2.80) * 0.85
elif flowers_kind == "Tulips" and flowers_count <= 80:
    money = flowers_count * 2.80
elif flowers_kind == "Narcissus" and flowers_count < 120:
    money = (flowers_count * 3) * 1.15
elif flowers_kind == "Narcissus" and flowers_count >= 120:
    money = flowers_count * 3
elif flowers_kind == "Gladiolus" and flowers_count < 80:
    money = (flowers_count * 2.50) * 1.20
elif flowers_kind == "Gladiolus" and flowers_count >= 80:
    money = flowers_count * 2.50

money = budget - money

if money >= 0:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_kind} and {money:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(money):.2f} leva more.")