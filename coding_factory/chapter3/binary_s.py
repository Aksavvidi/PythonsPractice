# Binary Search
def binary_search(my_array, element, start, end):
    # Αν το στοιχειο element δεν βρεθει στον πίνακα
    if start > end:
        return -1
    
    # mid position
    mid = (start + end) // 2

    # chack if i found the element
    if my_array[mid] == element:
        return mid
    elif my_array[mid] < element:
        return binary_search(my_array, element, mid +1, end)
    else:
        return binary_search(my_array, element, start, mid-1)
    
def main():
    my_array =[1, 2, 3, 4, 5, 6, 7]
    element = 2
    res = binary_search(my_array, 2, 0, len(my_array) - 1)

    print(res)

main()