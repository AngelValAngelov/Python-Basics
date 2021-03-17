budget = int(input())
season = input()
fisherman_count = int(input())
money = 0

if season == "Spring" and fisherman_count <= 6:
    money = 3000 * 0.90
elif season == "Spring" and 6 < fisherman_count <= 11:
    money = 3000 * 0.85
elif season == "Spring" and fisherman_count > 11:
    money = 3000 * 0.75
elif season == "Summer" and fisherman_count <= 6 or season == "Autumn" and fisherman_count <= 6:
    money = 4200 * 0.90
elif season == "Summer" and 6 < fisherman_count <= 11 or season == "Autumn" and 6 < fisherman_count <= 11:
    money = 4200 * 0.85
elif season == "Summer" and fisherman_count > 11 or season == "Autumn" and fisherman_count > 11:
    money = 4200 * 0.75
elif season == "Winter" and fisherman_count <= 6:
    money = 2600 * 0.90
elif season == "Winter" and 6 < fisherman_count <= 11:
    money = 2600 * 0.85
elif season == "Winter" and fisherman_count > 11:
    money = 2600 * 0.75

if fisherman_count % 2 == 0 and season != "Autumn":
    money *= 0.95

money = budget - money

if money >= 0:
    print(f"Yes! You have {money:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money):.2f} leva.")