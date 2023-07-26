#Populate a list
ages = [19, 23, 34, 45]

#Iterate over a list and access both the index 
# nad the value
for i, item in enumerate(ages):  #i = index item= age
    print(i, item)
    print(f"ages[{i}] is {item}")

print("------")

# With enhanced for
for age in ages:
    print(age)

# CRUD
grades = [1, 4, 8, 3, 9]

#Append
grades.append(10)

#Update
grades[0] = 2

#Delete
grades.remove(2)

#Search with value
if (4 in grades):
    print(4, "was found")

# Search for index
positionToUpdate = grades.index(10)
if positionToUpdate != -1:
    grades[positionToUpdate] = 7

print(grades)