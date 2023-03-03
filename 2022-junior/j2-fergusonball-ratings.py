number_of_players = int(input())

number_over_40 = 0
is_gold = True

for i in range(number_of_players):
    points = int(input())
    fouls = int(input())
    total = 5*points - 3*fouls
    if total > 40:
        number_over_40 += 1
    else:
        is_gold = False

if is_gold:
    print(f"{number_over_40}+")
else:
    print(number_over_40)
