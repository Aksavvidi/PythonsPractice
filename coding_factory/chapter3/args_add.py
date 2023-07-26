# Varargs
def my_add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

#function call
print(my_add())
print(my_add(10))
print(my_add(10, 20))
print(my_add(1, 2, 3, 4, 5))
