def main():
    x = int(input("enter a number : "))
    if is_even(x):
        print("your number is even.")
    else:
        print("your number is odd.")


def is_even(n):
    return n % 2 == 0
    # return True if n % 2 == 0 else False


main()
