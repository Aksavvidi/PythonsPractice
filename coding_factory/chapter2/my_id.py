num = 10 
a = 10
my_list = [1, 2]

print(id(num))
print(id(10))
print(id(a))

print("------")

print(id(my_list))
print(id([1,2]))
print(my_list is [1, 2])