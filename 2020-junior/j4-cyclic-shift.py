#j4 - cyclic shift (2020)

def find_shifts(text):
    shifts = []
    for i in range(len(text)):
        first = text[0]
        text = text[1:] + first
        shifts.append(text)
    return shifts


text = input()
string = input()
shifts = find_shifts(string)

found = False
for option in shifts:
    if option in text:
        found = True

if found:
    print("yes")
else:
    print("no")
