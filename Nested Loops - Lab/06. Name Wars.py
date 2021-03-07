name = input()
max_sum = 0
best_name = ""

while name != "STOP":
    current_sum = 0

    for letter in name:
        current_sum += ord(letter)
        if current_sum > max_sum:
            max_sum = current_sum
            best_name = name
    name = input()
print(f"Winner is {best_name} - {max_sum}!")