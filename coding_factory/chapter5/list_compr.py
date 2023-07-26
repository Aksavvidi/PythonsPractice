#declare a list of grades
grades = [7,5,9,10,3]

# map ()
upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]

print("Upscaled grades: ", upscaled_grades)   # Upscaled grades:  [8, 6, 10, 10, 4]

upscaled_grades2 = list(map(lambda grade: grade + 1 if grade <= 9 else grade, grades))

print("Upscaled grades2: ", upscaled_grades2)  # Upscaled grades2:  [8, 6, 10, 10, 4]

# Filter()
passed_grades = [grade for grade in upscaled_grades if grade >=5 ]
print("Passed grades",passed_grades)  #Passed grades [8, 6, 10, 10]

passed_grades2 = list(filter(lambda grade: grade >= 5, upscaled_grades))

print("Passed grades2",passed_grades2)   #Passed grades2 [8, 6, 10, 10]