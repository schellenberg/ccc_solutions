# j5 - nailed it (2017)

def find_number_of_boards_at_height(height, list_of_board_lengths):
    # need to make a copy of the list containing the counts of board lengths, since
    # we are going to be changing it every time this function is called
    lengths = list_of_board_lengths.copy()

    # to count how many boards of the current height, we can have two counters, one going up
    # and the other going down. For example, a board of length 50 could be made of lengths 1 and 49, 
    # or lengths 2 and 48, etc. If the height of the board is above 2000, however, we won't be
    # able to use some of the smaller pieces. That's what the max() call below takes care of.
    a = max(1, height - 2000)
    b = height - a

    how_many_boards = 0
    while a <= height/2:
        if a == b:
            # if both counters are the same, and there are 4 pieces of that size, we could make 2 boards.
            # if there are 5 pieces of that size, we can still only make 2 boards. We can use truncating
            # division to get just the integer value, without the decimal...
            boards = lengths[a] // 2
            # remove the number of boards used from our counter list, so we don't use them again later...
            lengths[a] -= boards * 2

            # add the number of possible boards to the accumulator variable
            how_many_boards += boards
        else:
            # say you are trying to count how many boards can be made of length 50, and a = 1, and b = 49
            # if there are 5 pieces of length 1 and 8 pieces of length 49, you can combine 5 pairs of them to 
            # make 5 boards of length 50. That is what the call to min() does below.
            boards = min(lengths[a], lengths[b])
            # remove the number of boards used from our counter list, so we don't use them again later...
            lengths[a] -= boards
            lengths[b] -= boards

            # add the number of possible boards to the accumulator variable
            how_many_boards += boards
        
        # increase one counter, and decrease the other. For example, if you are counting how many boards of
        # length 50 can be made, you would want to check 1 and 49, then 2 and 48, 3 and 47, etc...
        a += 1
        b -= 1
    
    return how_many_boards


number_of_boards = input()
raw_board_lengths = input().split()

# the following is called list comprehensions in Python, which I'm using to
# convert the length of the boards from a string to an integer
board_lengths = [int(board) for board in raw_board_lengths]

# an alternative syntax to do the same thing as the list comprehension version above:
# board_lengths = []
# for board in raw_board_lengths:
#     board_lengths.append(int(board))


# notice that the pieces of wood will all be from length 1 to 2000. 
# That means that the boards must be between length 2 and 4000.

# make a list to hold the number of pieces of wood of each height...
# since the boards are length 1 to 2000, make it contain index values up to 2000
heights = []
for i in range(0, 2001):
    heights.append(0)

# count how many of pieces of each height exist
for this_height in board_lengths:
    heights[this_height] += 1

# if you are unsure what the above does, comment out this debugging print line...
#print(heights)

# initialize variables to keep track of the longest fence, and the number of
# different heights it could have
max_boards = 0
heights_at_max_boards = 0

# since you are adding two pieces together, each of length 1 to 2000, the board
# (which is made up of EXACTLY two pieces of wood), must be between 2 to 4000 in length
# iterate through each of those options, and calculate how many boards can be made at
# each height
for counter in range(2, 4001):
    boards_at_this_height = find_number_of_boards_at_height(counter, heights)
    
    if boards_at_this_height > max_boards:
        # update the longest possible fence, and reset how many such fences can be made
        max_boards = boards_at_this_height
        heights_at_max_boards = 0
    
    if boards_at_this_height == max_boards:
        # if it's a tie, increment the number of possible fences by 1
        # note that this will happen if the first if statement occurs, which is why we 
        # set heights_at_max_boards to 0 above
        heights_at_max_boards += 1

print(max_boards, heights_at_max_boards)