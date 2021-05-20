#j5 - escape room (2020)

# this runs into a TLE problem for the last test cases, so only gets a 13/15
# I need to try a different strategy to make this pass all cases. Perhaps working backwards?
# Note to self: if taking time to try this again, maybe start from end location and work backwards to get to 1,1

import collections

m = int(input())
n = int(input())

coords = dict()
places_seen = set()

currX = 1
currY = 1
for row in range(m):
    data = input().split(" ")
    for num in data:
        location = f"{currY},{currX}"
        coords[location] = int(num)
        currX += 1
    currY += 1
    currX = 1

def get_factor_pairs(location):
    number = coords[location]
    
    pairs = set()
    the_max = int(number ** 0.5) + 1
    for i in range(1, the_max):
        if number % i == 0:
            j = int(number/i)
            
            this_location = f"{i},{j}"
            if i <= m and j <= n and this_location not in places_seen:
                pairs.add(this_location)

            this_location = f"{j},{i}"
            if i <= n and j <= m and this_location not in places_seen:
                pairs.add(this_location)
            
    return pairs

locations_to_check = collections.deque()
locations_to_check.append("1,1")

exit_found = False
while len(locations_to_check) > 0:
    location = locations_to_check.popleft()

    places_seen.add(location)
    r, c = location.split(",")
    if int(r) == m and int(c) == n:
        exit_found = True
        break
    elif int(r) <= m and int(c) <= n:
        new_locations = get_factor_pairs(location)
        for place in new_locations:
            if place not in locations_to_check and place not in places_seen:
                locations_to_check.append(place)

if exit_found:
    print("yes")
else:
    print("no")