month = input()
nights_count = int(input())
money_studio = 0
money_flat = 0

if month == "May" or month == "October":
    if nights_count > 7 and nights_count <= 14:
        money_studio = (nights_count * 50) * 0.95
        money_flat = nights_count * 65
    elif nights_count > 14:
        money_studio = (nights_count * 50) * 0.70
        money_flat = (nights_count * 65) * 0.90
    else:
        money_studio = nights_count * 50
        money_flat = nights_count * 65
elif month == "June" or month == "September":
    if nights_count > 14 :
        money_studio = (nights_count * 75.20) * 0.80
        money_flat = (nights_count * 68.70) * 0.90
    else:
        money_studio = nights_count * 75.20
        money_flat = nights_count * 68.70
elif month == "July" or month == "August":
    if nights_count > 14:
        money_studio = nights_count * 76
        money_flat = (nights_count * 77) * 0.90
    else:
        money_studio =nights_count * 76
        money_flat =nights_count * 77

print(f"Apartment: {money_flat:.2f} lv.\nStudio: {money_studio:.2f} lv.")


