str_one = input()
str_two = input()

current_letter = 0
new_str_one = ""

while str_two != new_str_one:
    if str_one[current_letter] == str_two[current_letter]:
        new_str_one += str_two[current_letter]
        current_letter += 1
        continue
    else:
        new_str_one += str_two[current_letter]
        current_letter += 1
    print(f"{new_str_one}", end="")
    for letter in str_one[current_letter : len(str_one)]:
        print(f"{letter}", end="")

    print()
