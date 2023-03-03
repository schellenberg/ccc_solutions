required_together = {}
not_together = {}

number_together = int(input())
for i in range(number_together):
    pair = input().split()
    first_student = pair[0]
    second_student = pair[1]
    
    if first_student not in required_together:
        required_together[first_student] = [second_student]
    else:
        required_together[first_student].append(second_student)

number_apart = int(input())
for i in range(number_apart):
    pair = input().split()
    first_student = pair[0]
    second_student = pair[1]
    
    if first_student not in not_together:
        not_together[first_student] = [second_student]
    else:
        not_together[first_student].append(second_student)
    

violations = 0
number_of_constraints = int(input())
for i in range(number_of_constraints):
    people = input().split()
    for person in people:
        #check if required partners are there
        if person in required_together:
            for needed_partner in required_together[person]:
                if needed_partner not in people:
                    violations += 1
        
        #check if people that can't be partnered are together
        if person in not_together:
            for cant_have_partner in not_together[person]:
                if cant_have_partner in people:
                    violations += 1
                    
# print(required_together)
# print(not_together)
print(violations)
