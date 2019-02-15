# j1 - tournament selection (2016)
number_of_wins = 0

for game in range(6):
    result = input()
    if result == "W":
        number_of_wins += 1

if number_of_wins >= 5:
    print(1)
elif number_of_wins >= 3:
    print(2)
elif number_of_wins >= 1:
    print(3)
else:
    print(-1)

