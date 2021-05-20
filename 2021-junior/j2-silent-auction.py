#j2 - silent auction (2021)

number_of_bids = int(input())
winning_name = ""
highest_bid = 0

for bid in range(number_of_bids):
    name = input()
    bid_amount = int(input())

    if bid_amount > highest_bid:
        winning_name = name
        highest_bid = bid_amount

print(winning_name)
