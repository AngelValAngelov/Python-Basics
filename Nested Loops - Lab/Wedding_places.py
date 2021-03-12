last_sector = input()
row_count_first_sector = int(input())
place_count_odd_row = int(input())
count = 0

for symbol in range(65,ord(last_sector) + 1):
    row_count_first_sector += 1
    for number in range(1 , row_count_first_sector):
        if number % 2 != 0:
            for place in range(97, 96 + place_count_odd_row + 1):
                count += 1
                print(f"{chr(symbol)}{number}{chr(place)}")
        else:
            for place in range(97,96 + place_count_odd_row + 3):
                count += 1
                print(f"{chr(symbol)}{number}{chr(place)}")
print(count)