budget = float(input())
flour_per_kg = float(input())

eggs_pack = flour_per_kg * 0.75
milk_per_litter = flour_per_kg * 1.25
kozunak_prise = flour_per_kg + eggs_pack + (milk_per_litter / 4)

kozunak_count = int(budget // kozunak_prise)
kozunak_receive = budget % kozunak_prise
eggs_count = 0

for kozunak in range(1, kozunak_count + 1):
    if kozunak % 3 == 0:
        eggs_count += 3
        eggs_count -= kozunak - 2
    else:
        eggs_count += 3

print(f"You made {kozunak_count} cozonacs! Now you have {eggs_count} eggs and {kozunak_receive:.2f}BGN left.")
