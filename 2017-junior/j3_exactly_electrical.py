#j3 - exactly electrical (2017)

coord = input()
coord_list = coord.split()
x = int(coord_list[0])
y = int(coord_list[1])

ending = input()
end_list = ending.split()
x2 = int(end_list[0])
y2 = int(end_list[1])

battery = int(input())

shortest_path = abs(x - x2) + abs(y - y2)

if battery >= shortest_path:
    if (battery - shortest_path) % 2 == 0:
        print("Y")
    else:
        print("N")
else:
    print("N")

