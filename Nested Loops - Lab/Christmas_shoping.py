import math

money_wanted = float(input())
fantacy_books = int(input())
horor_books = int(input())
romantic_books = int(input())
money_sellers = 0

all_money = fantacy_books * 14.90 + horor_books * 9.80 + romantic_books * 4.30
all_sum = all_money * 0.80

if all_sum >= money_wanted:
    money_sellers = math.floor((all_sum - money_wanted) * 0.10)
    all_sum -= money_sellers
    print(f"{all_sum:.2f} leva donated.")
    print(f"Sellers will receive {money_sellers}leva.")
else:
    all_sum = abs(all_sum - money_wanted)
    print(f"{all_sum:.2f} money needed.")