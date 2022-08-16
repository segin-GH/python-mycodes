



def main():

    while True:
        try:

            number = int(input("Enter a number : "))
            print("Your number is :", number)
            
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        
        

main()