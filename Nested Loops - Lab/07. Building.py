floor_count = int(input())
room_count = int(input())
floor = 0
last_room = 0

for floor in range(floor_count ,floor_count - 1, -1):
    for room in range(0 , room_count):
        print(f"L{floor}{room}", end=" ")

print()
for floor in range(floor_count - 1, 0 , -1):
    for room in range(0 , room_count):
        if floor % 2 == 0:
            print(f"O{floor}{room}", end=" ")
        else:
            print(f"A{floor}{room}", end=" ")
    print()