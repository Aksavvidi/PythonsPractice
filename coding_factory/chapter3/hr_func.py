# This is a square function
def square(x):
    return x * x  # x**2

#This is a cube function
def cube(x):
    return x *x *x

# Function witch takes as args an another function
def ho_func(func, nums):
    return[func(num) for num in nums]

def main():
    nums= [1, 2, 3, 4, 5]

    sq_nums = ho_func(square, nums)
    cb_nums = ho_func(cube, nums)

    print("Squared nums:", sq_nums)
    print("Cubed nums:" , cb_nums)

main()
