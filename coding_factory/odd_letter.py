
words = ["apple", "banana", "cherry", "fig", "melon"]
# filter() to choose only the odd letter-length worlds  
# len() return the number of letters in each world
#
list_of_odd_numbers_length_worlds = list(map(lambda x: len(x), filter(lambda x: len(x) % 2 != 0, words)))

print(list_of_odd_numbers_length_worlds)