# j3 - are we there yet (2018)

def sum_right_from(start, end):
    total = 0
    for i in range(start, end):
        total += distances[i]
    return total

def sum_left_from(start, end):
    total = 0
    for i in range(start-1, end-1, -1):
        total += distances[i]
    return total

data = input()

distances = data.split(" ")
for i in range(len(distances)):
    distances[i] = int(distances[i])


for i in range(0, 5):
    line = ""
    for j in range(0, 5):
        if i == j:
            line += "0 "
        elif i < j:
            line += str(sum_right_from(i, j)) + " "
        elif j < i:
            line += str(sum_left_from(i, j)) + " "
    print(line)

