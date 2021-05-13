l = int(input())
w = int(input())
peace = input()
peace_size = 1
all = l * w
peace_left = all

while peace_size > 0:
    if peace == "STOP":
        break
    else:
        peace = int(peace)
        peace_left -= peace
        if peace_left < 0:
            break
        peace = input()
        if peace == "STOP":
            break
if peace_left < 0:
    peace_left = abs(peace_left)
    print(f"No more cake left! You need {peace_left} pieces more.")
else:
    peace_left = abs(peace_left)
    print(f"{peace_left} pieces are left.")