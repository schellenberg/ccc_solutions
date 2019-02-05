# j1 - telemarketer or not (2018)
a = int(input())
b = int(input())
c = int(input())
d = int(input())

first_pattern = a == 8 or a == 9
second_pattern = d == 8 or d == 9
third_pattern = b == c

if first_pattern and second_pattern and third_pattern:
    print("ignore")
else:
    print("answer")