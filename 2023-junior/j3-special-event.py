n = int(input())
#ans[i] is the number of people who can make it on each day
ans = [0]*5
for i in range(n):
    x = input()
    for j in range(5):
        if x[j] == 'Y':
            ans[j] += 1

mx = [0]
for i in range(1,5):
	#if the day we're looking at is better than all the others we've looked at, thats our only date
	#if its equal to the biggest date, we can add it to our list
    if ans[i]>ans[mx[0]]:
        mx = [i]
    elif ans[i]==ans[mx[0]]:
        mx.append(i)

#i+1 instead of i, since the problem is 1-indexed
#the * turns the list into multiple arguments, e.g. *[1,2,3,4] = 1,2,3,4
#seperate by commas
print(*[i+1 for i in mx],sep=',')

