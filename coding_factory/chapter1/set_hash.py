# Set hash()
 
s = {1, "Coding", [1, 2]}  # It must be hashable the 'list' isn't hashable

print(s) # TypeError: unhashable type: 'list'