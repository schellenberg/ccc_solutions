# j1 - winning score (2019)

apple_3s = int(input())
apple_2s = int(input())
apple_1s = int(input())

banana_3s = int(input())
banana_2s = int(input())
banana_1s = int(input())

apple_score = apple_3s * 3 + apple_2s * 2 + apple_1s
banana_score = banana_3s * 3 + banana_2s * 2 + banana_1s

if apple_score > banana_score:
    print("A")
elif banana_score > apple_score:
    print("B")
else:
    print("T")