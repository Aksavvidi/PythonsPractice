# Extended Unpacking
my_list = [1, 2, 3, 4, 5]

a, *b = my_list

print(f"a ={a}, b = {b}")   #a =1, b = [2, 3, 4, 5]