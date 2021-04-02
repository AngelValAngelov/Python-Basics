open_tabs = int(input())
calary = int(input())

for website in range(open_tabs):
    text = input()
    if text == "Facebook":
        calary -= 150
        if calary <= 0:
            calary = 0
            break
    if text == "Instagram":
        calary -= 100
        if calary <= 0:
            calary = 0
            break
    if text == "Reddit":
        calary -= 50
        if calary <= 0:
            calary = 0
            break
if calary == 0:
    print("You have lost your salary.")
else:
    print(calary)