# j2 - magic squares (2016)

def check_if_magic(square):
    the_sum = sum(square[0])
    for counter in range(4):
        if sum(square[counter]) != the_sum:
            return False
    
    for column in range(4):
        this_column = []
        for row in range(len(square)):
            this_column.append(square[row][column])
        
        if sum(this_column) != the_sum:
            return False
    
    return True
    

grid = []
for counter in range(4):
    row = input()
    row_numbers_as_str = row.split()
    current_row = []
    for number in row_numbers_as_str:
        current_row.append(int(number))
    grid.append(current_row)
    
magic_sum = sum(grid[0])

if check_if_magic(grid):
    print("magic")
else:
    print("not magic")
