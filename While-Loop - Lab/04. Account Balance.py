pay_count = int(input())
money = float(input())
resolt = 0

while pay_count > 0:
    if money < 0:
        print("Invalid operation!")
        break
    resolt = resolt + money
    print(f"Increase: {money:.2f}")
    pay_count -= 1
    if pay_count == 0:
        break
    else:
        money = float(input())

print(f"Total: {resolt:.2f}")
