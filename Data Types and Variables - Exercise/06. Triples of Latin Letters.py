n = int(input())

for number in range(97 , 97 + n):
    for numm in range(97 , 97 + n):
        for num in range(97 , 97 + n):
            print(f"{chr(number)}{chr(numm)}{chr(num)}", end="")
            print()
