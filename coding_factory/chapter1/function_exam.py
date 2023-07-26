def get_average_of(num1, num2, num3):
    return "{:.2f}".format((num1 + num2 + num3) / 3)

def main():
    num1 = 10
    num2 = 15
    num3 = 16

    average = get_average_of(num1, num2, num3)
    print(average)

main()
