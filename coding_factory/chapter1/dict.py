#CRUD Functions on dicts

# not to do
# d = {1: True, "one": "ONE", "PI": 3.14}

# Populate a dictionary
products = {1:"apples", 2:"bananas", 3:"pears"} # Dict:  {1: 'apples', 2: 'bananas', 3: 'pears'}
print("Dict: ", products)

# Insert  (works directly)
products[4] = "oranges"
print("Dict after insert oranges: ", products) #Dict after insert oranges:  {1: 'apples', 2: 'bananas', 3: 'pears', 4: 'oranges'}

# Update
products[1] = "melon"
print("Dict after update key[1] to melon: ", products) #Dict after update key[1] to melon:  {1: 'melon', 2: 'bananas', 3: 'pears', 4: 'oranges'} 
# Delete
del products[2]
print("Dict after deleting key-value pair with key= 2: ", products) # Dict after deleting key-value pair with key= 2:  {1: 'melon', 3: 'pears', 4: 'oranges'}

# Access a specific key:value pair
print("Access a specific key:value pair key=4: ", products[4]) # Access a specific key:value pair key=4:  oranges


