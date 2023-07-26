# Set Example 02
# add(), remove()

#Δηλωση ενός συνόλου
s ={5, 10, 10, 10, 5, "Coding", 3.14, True, "factory"}
print("Set after declaration: ",s)
# print(len(s))  prints 6 

#add some  items
s.add(True)
print("1. Set after add: ", s)

s.add(100)
print("2. Set after add: ", s)

# Remove item
s.remove(True)
print("Set after remove 'True' : ", s)

# check with membership operator: in
print("Check if 10 exist:", 10 in s)

