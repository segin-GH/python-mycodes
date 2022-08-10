

def main():

    while(True):

        x = int(input("Enter x : "))
        y = int(input("Enter y : "))

        opp = input("Enter the opperation( +, -, *, /, % ) : ") 
        
        if(opp == "+"):
            print(x + y)

        elif(opp == "-"):
            print(x - y)
        
        elif(opp == "*"):
            print(x * y)

        elif(opp == "/"):
            print(x / y)
        
        elif (opp == "%"): 
            print(x % y)
        else:
            print("Enter a valid operation")

    



main()