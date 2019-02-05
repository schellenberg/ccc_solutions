# j4 - sunflowers (2018)

def pretty_print_grid(the_grid):
    pretty = ""
    for y in range(len(the_grid)):
        row = ""
        for x in range(len(the_grid[y])):
            row += str(the_grid[y][x]) + " "
        pretty += row + "\n"
    print(pretty)

def create_empty_grid(size):
    grid = []
    for i in range(size):
        column = []
        for j in range(size):
            column.append(0)
        grid.append(column)
    return grid

def change_row(grid, row, new_values):
    numbers_to_add = new_values.split(" ")
    for x in range(len(numbers_to_add)):
        grid[row][x] = int(numbers_to_add[x])
    return grid

def rotate_90(grid):
    new_grid = create_empty_grid(len(grid))
    current_x = 0
    for y in range(len(grid)):
        current_y = len(grid) - 1
        for x in range(len(grid[y])):
            new_grid[y][x] = grid[current_y][current_x]
            current_y -= 1
        current_x += 1
    return new_grid

def check_rules(grid):
    return rows_okay(grid) and columns_okay(grid)

def rows_okay(grid):
    for y in range(len(grid)):
        for x in range(1, len(grid[y])):
            if grid[y][x-1] > grid[y][x]:
                return False
    return True

def columns_okay(grid):
    for x in range(len(grid[0])):
        for y in range(1, len(grid)):
            if grid[y-1][x] > grid[y][x]:
                return False
    return True

grid_size = int(input())
grid = create_empty_grid(grid_size)

for the_row in range(grid_size):
    this_row = input()
    grid = change_row(grid, the_row, this_row)


while check_rules(grid) == False:
    grid = rotate_90(grid)
    
pretty_print_grid(grid)