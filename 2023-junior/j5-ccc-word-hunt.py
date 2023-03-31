word = input()
r = int(input())
c = int(input())

grid = [input().split() for i in range(r)]

#all 8 possible directions, notated as a difference in x and y values after 1 step in the direction
dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,1,-1,-1,1]

#arrange your direction array the right way so you can do this:
def get_pr(i):
    if i<4:
        return [(i+1)%4,(i-1)%4]
    return [(i-3)%4+4, (i-5)%4+4]

#depth-first search
#x and y is the position, ind is the index in the word, dirc is the direction, ch is whether the direction has changed
#returns number of valid words
def dfs(x,y,ind,dirc,ch):
    #base case: we are at the end of the word!
    if ind==len(word)-1:
        return 1
    #check whether next letter is good, if so, recursively search
    ans = 0
    nx = x+dx[dirc]
    ny = y+dy[dirc]
    #check if position is in bounds
    if 0<=nx and nx<r and 0<=ny and ny<c:
        #check if letter is valid
        if word[ind+1]==grid[nx][ny]:
            ans = dfs(nx,ny,ind+1,dirc,ch)
    #if we have already changed, we can't change again, so we're done
    if ch:
        return ans

    #iterate over each direction
    for i in get_pr(dirc):
        nx = x+dx[i]
        ny = y+dy[i]
        #check if position is in bounds
        if 0<=nx and nx<r and 0<=ny and ny<c:
            #check if letter is valid
            if word[ind+1]==grid[nx][ny]:
                ans += dfs(nx,ny,ind+1,i,1)
    
    return ans

res = 0
#only search if we have found the first 2 letters
for i in range(r):
    for j in range(c):
        if grid[i][j]==word[0]:
            for dr in range(8):
                nx = i+dx[dr]
                ny = j+dy[dr]
                if 0<=nx and nx<r and 0<=ny and ny<c:
                    if grid[nx][ny]==word[1]:
                        res += dfs(nx,ny,1,dr,0)

print(res)
