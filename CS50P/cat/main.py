

from pickle import TRUE


def main():
    number = get_number()
    print_meow(number)


def get_number():
    while True:
        number = int(input("Enter a number : "))
        if number > 0:
            return number
            

def print_meow(number):
    for _ in range(number):
        print("meow")

main()




