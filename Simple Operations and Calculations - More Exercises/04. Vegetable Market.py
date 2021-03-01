price_vegetable_per_kg = float(input())
price_fruits_per_kg = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

sum_leva = (vegetables_kg * price_vegetable_per_kg) + (fruits_kg * price_fruits_per_kg)
sum_euro = sum_leva / 1.94

print(f"{sum_euro:.2f}")