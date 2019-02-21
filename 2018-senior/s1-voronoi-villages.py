number_of_villages = int(input())
village_locations = []

for i in range(number_of_villages):
    this_village = int(input())
    village_locations.append(this_village)

village_locations.sort()


neighborhoods = []
for counter in range(number_of_villages):
	if counter == 0 or counter == number_of_villages-1:
		pass
	else:
		left_distance = abs( village_locations[counter-1] - village_locations[counter]) / 2
		right_distance = abs( village_locations[counter] - village_locations[counter+1]) / 2
		this_size = left_distance + right_distance
		print(left_distance, right_distance)
		neighborhoods.append(this_size)

print(neighborhoods)

print(min(neighborhoods))