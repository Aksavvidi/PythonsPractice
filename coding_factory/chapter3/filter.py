# filter func with lambda

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers_iterator = filter(lambda x: x % 2 == 0, numbers)
    odd_numbers_iterator = filter(lambda x: x % 2 != 0, numbers)

    for even_num in even_numbers_iterator:
        print(even_num, end=" ")
        
    print()
    for odd_num in odd_numbers_iterator:
        print(odd_num, end=" ")

    print()

    #Converting the iterator to a list
    list_even_nums = list(even_numbers_iterator)
    for num in list_even_nums:
        print(num, end=" ")


main()

