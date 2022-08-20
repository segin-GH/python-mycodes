



def main ():
    # name = input("enter your name ? ")
    # file = open("name.txt","a")
    # file.write(f"{name}\n")
    # file.close()

    printName()



def printName():
    name = []
    with open("name.txt", "r") as file:
        for line in file:
            name.append(line.rstrip())

    for line in sorted(name):
        print(f"hello,{line}")



if __name__ == "__main__":
    main()