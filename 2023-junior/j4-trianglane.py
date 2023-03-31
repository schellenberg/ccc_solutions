n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
#left and right edges
ans = a[0]+a[-1]+b[0]+b[-1]

#edges between top and bottom
for i in range(0,n,2):
    ans += a[i]!=b[i]

#edges between triangles on the same row
for i in range(n-1):
    ans += (a[i]!=a[i+1])+(b[i]!=b[i+1])

#top and bottom edges
for i in range(1,n,2):
    ans += a[i]+b[i]

print(ans)
