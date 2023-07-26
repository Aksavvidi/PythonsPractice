# gets 3 args and return the average value

def get_average(num1, num2, num3):
    #block code
    total = num1 + num2 + num3
    average = total / 3
    return average

# Αρχικοποιώ τισ μεταβλητες 

a = 10
b = 15
c = 16

# Call function and insert the result in a variable

result = get_average(a,b,c)

print("Average of: ", a, b, c, "is equal to:", result)