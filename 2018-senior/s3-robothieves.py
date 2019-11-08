# s3 - robothieves (2018)

from dataclasses import dataclass

@dataclass
class Cell:
    x: int
    y: int
    distance: int

def find_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "S":
                return (x, y)

def check_nesw(grid, x, y, current_distance):
    open_spots = []
    if grid[y+1][x] == ".":
        open_spots.append((x, y+1, current_distance+1))
    if grid[y-1][x] == ".":
        open_spots.append((x, y-1, current_distance+1))
    if grid[y][x+1] == ".":
        open_spots.append((x+1, y, current_distance+1))
    if grid[y][x-1] == ".":
        open_spots.append((x-1, y, current_distance+1))
    
    if open_spots != []:
        return open_spots

raw_dimensions = input()
dimensions = raw_dimensions.split()
rows = int(dimensions[0])
cols = int(dimensions[1])

grid = []
for counter in range(rows):
    row = list(input())
    grid.append(row)

#print(grid)

start_x, start_y = find_start(grid)

print(start_x, start_y)

distances_away = [[]]
distances_away.append(check_nesw(grid, start_x, start_y))
print(distances_away)

next_level = []
for coord in distances_away[1]:
    new_spots = check_nesw(grid, coord[0], coord[1])
    if new_spots != None:
        next_level.append(new_spots)

if next_level != []:
    distances_away.append(next_level)

print(distances_away)