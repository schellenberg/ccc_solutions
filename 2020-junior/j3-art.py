#j3 - art (2020)

n = int(input())

xCoords = []
yCoords = []

for i in range(n):
    x, y = input().split(",")
    x = int(x)
    y = int(y)
    
    xCoords.append(x)
    yCoords.append(y)

bottomLeftX = min(xCoords) - 1
bottomLeftY = min(yCoords) - 1

topRightX = max(xCoords) + 1
topRightY = max(yCoords) + 1

print(f"{bottomLeftX},{bottomLeftY}")
print(f"{topRightX},{topRightY}")
