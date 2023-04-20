def main():
    name = input("what is your name? ")
    match name:
        case "harry" | "hermione" | "ron" | "ginny":
            print("griffindor")
        case "draco":
            print("slytherin")
        case _:
            print("who ?")

    # match name:
    #     case "harry":
    #         print("griffindor")
    #     case "ron":
    #         print("griffindor")
    #     case "hermione":
    #         print("griffindor")
    #     case "draco":
    #         print("slytherin")
    #     case _:
    #         print("who ?")


main()
