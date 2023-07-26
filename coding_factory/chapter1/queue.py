import re
# Insert an item in index (0) and pop it from index (0), First in first out 
queue = []
num = 0

def insert(tail, item):
    tail.insert(0, item)

def pop(tail):
    if tail:
        return tail.pop(0) # Pop the item of the 1st index (0)
    else:
        print("There is nothing in the Queue")

def print_menu():
    print("1. Insert on the top")
    print("2. Get from the top")
    print("q/Q for Quit")

def get_choice():
    return input("Please provide a choice\n")

def main():
    choice = 0
    num = 0
    out_num = 0

    while True:
        print_menu()
        choice = get_choice()

        if not choice:
            continue

        if choice == 'q' or choice == 'Q':
            break

        pattern = r'^\d+$' # Only Numeric choice
        match = re.match(pattern, choice)

        if not match:
            print("Error in choice")
            continue

        choice = int(choice)

        match choice:
            case 1:
                num = input("Please insert a num")
                match = re.match(pattern, num)

                if not match:
                    print("Error in num")
                    continue

                num = int(num)
                insert(queue, num)
                print(num, "Insert on the stack")

            case 2: 
                out_num = pop(queue)
                print("You got:", out_num)

            case _:
                print("Not valid choice")

    print("Goodbye!!")

if __name__== '__main __':
    main()


main()
