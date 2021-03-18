budget =  float(input())
season = input()
where = ""
money = 0
place = ""

if budget <= 100:
    where = "Bulgaria"
    if season == "summer":
        place = "Camp"
        money = budget * 0.30
    else:
        place = "Hotel"
        money = budget * 0.70
elif budget <= 1000:
    where = "Balkans"
    if season == "summer":
        place = "Camp"
        money = budget * 0.40
    else:
        place = "Hotel"
        money = budget * 0.80
else:
    where = "Europe"
    place = "Hotel"
    money = budget * 0.90

print(f"Somewhere in {where}\n{place} - {money:.2f}")