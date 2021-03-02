w = float(input())
h = float(input())

hall_h = (h * 100) - 100
school_table = hall_h // 70
school_h = (w * 100) // 120

seats = school_table * school_h - 3

print(f"{seats:.0f}")