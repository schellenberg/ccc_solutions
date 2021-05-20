# Name: Yusra Hassan
# Date: April 5th - April 15th, 2021
# Description: J5 Solution (Find if its possible to escape a room given a grid of cells with a specific way of moving)
# Purpose: CCC practice (level 5 question)
# Credit: Inspiration from Luke Zhang's https://github.com/Luke-zhang-04/CCC-Problems/blob/master/2020/s2.py

# Variables
escapability = "no"
keyFound = False
grid = []
visited = []

# Input with error handling
M = int(input())
N = int(input())
for i in range(M):
    # get input, error handle, split, error handle, cast items to int
    row = input().split()
    for j in range(N):
        row[j] = int(row[j])
    grid.append(row)

# Function to get numbers a certain position can lead to
def getNums(cell):
    global M, N, grid
    factors = []
    numbers = []
    
    # Get smallest number possible to look for factors in
    num = M
    if M < N:
        num = N
    if M > cell:
        num = cell
    
    # Get factors
    for i in range(1, num + 1):
        if cell % i == 0:
            factors.append(i)
    
    # Turn factors into corresponding numbers for each pair
    for i in factors:
        rltdFactor = cell // i
        if i <= M and rltdFactor <= N:
            numbers.append(grid[i - 1][rltdFactor - 1])
    
    return numbers

# Main function
def canYouEscape(cell):
    pSteps = getNums(cell) # list of possible next step numbers a given number could go to
    if cell == M * N or M * N in pSteps: # check if the current number or its next steps are an escape value
        return True
    else:
        for step in pSteps: # go through each possible next step
            if getNums(step) != [] and step not in visited: # make sure this path continues and has not been taken already
                visited.append(step)
                if canYouEscape(step): # recurse until no possible next steps or a solution path is found
                    return True
    return False

# Check if the value leading to the exit is even present in the grid
for i in grid:
    if M * N in i:
        keyFound = True
        break

# If the value is present, use the canYouEscape function to see if the entrance of the escape room leads to it
if keyFound:
    initial = grid[0][0]
    visited.append(initial) # append the initial value to the visited list
    if canYouEscape(initial):
        escapability = "yes"
print(escapability)