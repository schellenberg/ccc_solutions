# j3 - cold compress (2019)

def count_number_of_first_character(some_string):
    starting_char = some_string[0]
    counter = 0
    while counter < len(some_string) and starting_char == some_string[counter]:
        counter += 1
    return counter

def encode_string(message):
    encoded_message = ""
    counter = 0
    while counter < len(message):
        how_many = count_number_of_first_character(message[counter:])
        encoded_message += str(how_many) + " " + str(message[counter]) + " "
        counter += how_many
    print(encoded_message)

lines = int(input())

for counter in range(lines):
    data = input()
    encode_string(data)
