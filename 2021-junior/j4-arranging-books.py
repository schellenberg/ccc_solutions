#j4 - arrranging books (2021)

books = input()

number_of_large = books.count("L")
number_of_medium = books.count("M")
number_of_small = books.count("S")

mediums_in_large_section = books.count("M", 0, number_of_large)
smalls_in_large_section = books.count("S", 0, number_of_large)

larges_in_medium_section = books.count("L", number_of_large, number_of_large + number_of_medium)
smalls_in_medium_section = books.count("S", number_of_large, number_of_large + number_of_medium)

# add all the swaps up, but subtract by the number of "efficient" swaps (where swapping puts both in the right place)
total_swaps = mediums_in_large_section + smalls_in_large_section + \
              larges_in_medium_section + smalls_in_medium_section - \
              min(larges_in_medium_section, mediums_in_large_section)

print(total_swaps)