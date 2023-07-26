# Reduce 
from functools import reduce

def main():
    my_ints = [1, 2, 3, 4, 5]

    #calculate the mul of nums in the list
    result = reduce(lambda x, y: x * y, my_ints)

    # print results
    print("Result: ", result)

main()