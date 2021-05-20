product = input()
city = input()
quantity = float(input())
result = 0

if city == "Sofia" and product == "coffee":
    result = 0.50 * quantity
elif city == "Sofia" and product == "water":
    result = 0.80 * quantity
elif city == "Sofia" and product == "beer":
    result = 1.20 * quantity
elif city == "Sofia" and product == "sweets":
    result = 1.45 * quantity
elif city == "Sofia" and product == "peanuts":
    result = 1.60 * quantity
elif city == "Plovdiv" and product == "coffee":
    result = 0.40 * quantity
elif city == "Plovdiv" and product == "water":
    result = 0.70 * quantity
elif city == "Plovdiv" and product == "beer":
    result = 1.15 * quantity
elif city == "Plovdiv" and product == "sweets":
    result = 1.30 * quantity
elif city == "Plovdiv" and product == "peanuts":
    result = 1.50 * quantity
if city == "Varna" and product == "coffee":
    result = 0.45 * quantity
elif city == "Varna" and product == "water":
    result = 0.70 * quantity
elif city == "Varna" and product == "beer":
    result = 1.10 * quantity
elif city == "Varna" and product == "sweets":
    result = 1.35 * quantity
elif city == "Varna" and product == "peanuts":
    result = 1.55 * quantity

print(result)