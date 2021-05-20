#j3 - secret instructions (2021)

instructions = ""

while True:
    instructions = input()
    if instructions == "99999":
        break

    direction_sum = int(instructions[0]) + int(instructions[1])
    if direction_sum % 2 == 1:
        direction = "left"
    elif direction_sum % 2 == 0 and direction_sum != 0:
        direction = "right"

    message = f"{direction} {instructions[2:]}"
    print(message)
