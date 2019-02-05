# j2 - occupy parking (2018)
number_of_spaces = int(input())
yesterday = input()
today = input()

total_occupied_both_days = 0
for space in range(len(yesterday)):
    if yesterday[space] == "C" and today[space] == "C":
        total_occupied_both_days += 1

print(total_occupied_both_days)
