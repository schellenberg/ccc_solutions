# j3 - hidden palindrome (2016)

def check_if_palindrome(word):
    if len(word) == 1:
        return True
    
    forward = word
    backward = forward[::-1]
    
    return forward == backward
        

word = input()
possibles = []

for i in range(len(word)):
    for j in range(len(word), -1, -1):
        if (i < j):
#            print(i, j, word[i:j])
            possibles.append(word[i:j])

for j in range(len(word), -1, -1):
    for i in range(len(word)):
        if i < j:
#            print(i, j, word[i:j])
            possibles.append(word[i:j])
            

longest = 0
for some_word in possibles:
    if check_if_palindrome(some_word) and len(some_word) > longest:
        longest = len(some_word)

print(longest)