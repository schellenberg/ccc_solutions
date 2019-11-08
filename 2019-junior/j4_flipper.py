# j4 - flipper (2019)


# a | b
# c | d

a = 1
b = 2
c = 3
d = 4


instructions = input()

for task in instructions:
    if task == "H":
        temp = a
        a = c
        c = temp
        
        temp = b
        b = d
        d = temp
        
    elif task == "V":
        temp = a
        a = b
        b = temp
        
        temp = c
        c = d
        d = temp
    
print(a, b)
print(c, d)