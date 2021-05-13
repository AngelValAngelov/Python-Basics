steps = 10000
total = 0
final_steps = 0

while total < steps:
    moving_steps = input()
    if moving_steps != "Going home":
        moving_steps = int(moving_steps)
        total += moving_steps
        final_steps = total
        if total >= steps:
            break
    else:
        moving_steps = int(input())
        final_steps = total + moving_steps
        break
if steps > final_steps:
    print(f"{steps - final_steps} more steps to reach goal.")
else:
    print("Goal reached! Good job!")