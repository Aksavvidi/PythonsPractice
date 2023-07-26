# CRUD

#Create
grades = [1, 4, 10, 7, 5]
print("Grades: ", grades)

#Append
grades.append(8)
print("Grades after append: ", grades)

#Update
grades[1] = 5
print("Grades after update: ", grades)

#Delete
grades.remove(1)
print("Grades after remove: ", grades)


#Search with value
if (10 in grades):
    print(10, "was found")

# Search for index
if 10 in grades:
    positionToUpdate = grades.index(10)
    grades[positionToUpdate] = 9.5

print(grades)