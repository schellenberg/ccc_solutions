#j5 - modern art (2021)

rows = int(input())
cols = int(input())
strokes = int(input())

rows_flipped = dict()
cols_flipped = dict()

for i in range(strokes):
    direction, location = input().split(" ")
    location = int(location)

    if direction == "R":
        if location in rows_flipped:
            rows_flipped[location] = rows_flipped[location] + 1
        else:
            rows_flipped[location] = 1

    else:
        if location in cols_flipped:
            cols_flipped[location] = cols_flipped[location] + 1
        else:
            cols_flipped[location] = 1

number_of_gold = 0
for y in range(1, rows+1):
    for x in range(1, cols+1):
        total_flips = 0
        if y in rows_flipped:
            total_flips += rows_flipped[y]
        if x in cols_flipped:
            total_flips += cols_flipped[x]

        if total_flips % 2 == 1:
            number_of_gold += 1
print(number_of_gold)