#Populate a tuple

ages =( 30, 40, 25, 27)

#print(type(ages)) # <class 'tuple'>

# Traverse
#Απλή For
for index, age in enumerate(ages):  # age = item
    print(f"{index} : {age}")

# Enhanced For
for age in ages:
    print(age)