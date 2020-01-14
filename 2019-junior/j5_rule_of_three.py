# j5 - rule of three (2019)

# create list of rules
rules = []
for counter in range(1, 4):
    some_rule = input().split()
    rules.append([some_rule[0], some_rule[1], counter])

# get number of steps, starting value, and ending value
steps, starting, GOAL = input().split()
steps = int(steps)

# keep track of which sequences have been seen, to avoid needless repetition
#  originally, I used a list for this, but I got a Time Limit Exceeded error, and only got 14/15
#  so, I converted this part into the more efficient set() data type, which only allows for unique elements
#  look up sets here: https://realpython.com/python-sets/
sequences_seen = set()

def solver(remaining_steps, sequence, history):
    # might be helpful to understand what is going on if you uncomment the print statement below
    # print(remaining_steps, sequence, history)

    # base case if successfully found it
    if remaining_steps == 0 and sequence == GOAL:
        return history
    
    # base case if didn't find it and ran out of remaining steps
    elif remaining_steps == 0:
        return False
    
    # one last base case / exit clause...
    #  if we still have remaining steps, check to see if the current sequence
    #  has already been considered (otherwise, we calculate WAY too many options)
    # this should only matter for the final marks (last efficiency check)
    current = (sequence, remaining_steps)  # this is a tuple (which is an immutable list)
    if current in sequences_seen:
        return False
    else:
        sequences_seen.add(current)
    
    
    # iterate through each rule and find where it can be used on current sequence
    for rule, substitution, rule_number in rules:
        possible_positions = find_all_indices(sequence, rule)
        for index in possible_positions:
            # determine the new value of the sequence
            new_sequence = sequence[:index] + substitution + sequence[index + len(rule):]
            
            # make a new version of the history list, so we don't just point to the same one...
            modified_history = history.copy()
            modified_history.append([rule_number, index + 1, new_sequence])
            
            # recursively call this function, but decrease number of remaining steps
            result = solver(remaining_steps - 1, new_sequence, modified_history)
            
            if result:  # will only be True if we have found the solution, in which case end we should stop
                return result
        
    
def find_all_indices(sequence, rule_to_find):
    indices_list = []
    current_index = 0
    while True:
        # look from the current index location to see if the rule exists to the right
        current_index = sequence.find(rule_to_find, current_index)
        if current_index == -1:
            return indices_list
        else:
            indices_list.append(current_index)
        
        # move forward one index value to check further on in the sequence
        current_index += 1
        

# recursively call function, then print result
answer = solver(steps, starting, [])
for step in answer:
    print(step[0], step[1], step[2])