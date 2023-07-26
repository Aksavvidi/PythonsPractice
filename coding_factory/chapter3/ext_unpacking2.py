# Extended Unpacking 2
my_list = [1, 2, 3, 4, 5]

a, *b, c = my_list      #Only one unpack operation '*' allowed in list

print(f"a ={a}, b = {b}, c = {c}")  #a =1, b = [2, 3, 4], c = 5