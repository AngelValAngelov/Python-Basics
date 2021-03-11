days = int(input())
sport = ""
all_result = 0.00
game_lost = 0
game_win = 0
day_win = 0
day_lost = 0
money_per_day = 0
for day in range(1 , days + 1):
    game_win = 0
    game_lost = 0
    sport = input()
    while sport != "Finish":
        result = input()
        if result == "win":
            game_win += 1
        elif result == "lose":
            game_lost += 1
        sport = input()
    if game_win > game_lost:
        day_win += 1
        money_per_day = (game_win * 20) * 1.10
        all_result += money_per_day
    else:
        day_lost += 1
        money_per_day = game_win * 20
        all_result += money_per_day
if day_win > day_lost:
    all_result *= 1.20
    print(f"You won the tournament! Total raised money: {all_result:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {all_result:.2f}")

