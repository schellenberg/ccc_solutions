#j2 - shifty sum (2017)
original_number = int(input())
number_of_shifts = int(input())

sum = original_number

for counter in range(number_of_shifts):
    sum += original_number*10
    original_number *= 10

print(sum)
