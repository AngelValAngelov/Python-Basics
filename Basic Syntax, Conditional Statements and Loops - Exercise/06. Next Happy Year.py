import sys

number = int(input()) + 1

year = number

digit_0 = 0
digit_1 = 0
digit_2 = 0
digit_3 = 0
digit_4 = 0
digit_5 = 0
digit_6 = 0
digit_7 = 0
digit_8 = 0
digit_9 = 0

for num in range(number , sys.maxsize):
    num = str(num)
    for digit in num:
        if digit == "0":
            digit_0 += 1
        elif digit == "1":
            digit_1 += 1
        elif digit == "2":
            digit_2 += 1
        elif digit == "3":
            digit_3 += 1
        elif digit == "4":
            digit_4 += 1
        elif digit == "5":
            digit_5 += 1
        elif digit == "6":
            digit_6 += 1
        elif digit == "7":
            digit_7 += 1
        elif digit == "8":
            digit_8 += 1
        elif digit == "9":
            digit_9 += 1

    if digit_0 > 1 or digit_1 > 1 or digit_2 > 1 or digit_3 > 1 or digit_4 > 1 or digit_5 > 1 or digit_6 > 1 or digit_7 > 1 or digit_8 > 1 or digit_9 > 1:
        digit_0 = 0
        digit_1 = 0
        digit_2 = 0
        digit_3 = 0
        digit_4 = 0
        digit_5 = 0
        digit_6 = 0
        digit_7 = 0
        digit_8 = 0
        digit_9 = 0
        continue
    else:
        print(int(num))
        break
