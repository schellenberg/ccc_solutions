# j2 - time to decompress (2019)

lines = int(input())

for counter in range(lines):
    info = input()
    number = int(info.split()[0])
    symbol = info.split()[1]
    print(symbol * number)

