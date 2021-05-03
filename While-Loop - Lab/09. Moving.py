width = int(input())
length = int(input())
height = int(input())
boxes_count = input()

all_space = width * length * height

while all_space >= 0:
    if boxes_count != "Done":
        boxes_count = int(boxes_count)
        all_space -= boxes_count
        if all_space < 0:
            break
        boxes_count = input()
    else:
        print(f"{abs(all_space)} Cubic meters left.")
        break
if boxes_count != "Done":
    print(f"No more free space! You need {abs(all_space)} Cubic meters more.")