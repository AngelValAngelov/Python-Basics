deg = float(input())
time = input()
outfit = ""
shoes = ""

if time == "Morning" and 10 <= deg <= 18:
    outfit = "Sweatshirt"
    shoes = "Sneakers"
elif time == "Morning" and 18 < deg <= 24:
    outfit = "Shirt"
    shoes = "Moccasins"
elif time == "Morning" and deg >= 25:
    outfit = "T-Shirt"
    shoes = "Sandals"
elif time == "Afternoon" and 10 <= deg <= 18:
    outfit = "Shirt"
    shoes = "Moccasins"
elif time == "Afternoon" and 18 < deg <= 24:
    outfit = "T-Shirt"
    shoes = "Sandals"
elif time == "Afternoon" and deg >= 25:
    outfit = "Swim Suit"
    shoes = "Barefoot"
elif time == "Evening" and 10 <= deg <= 18:
    outfit = "Shirt"
    shoes = "Moccasins"
elif time == "Evening" and 18 < deg <= 24:
    outfit = "Shirt"
    shoes = "Moccasins"
elif time == "Evening" and deg >= 25:
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {deg:.0f} degrees, get your {outfit} and {shoes}.")

