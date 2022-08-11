

def main():

    try:
        x = int((input("Enter a number : ")))
    except ValueError:
        print("plz enter a integer.")
    else:
        print("your number is :",x)
main()