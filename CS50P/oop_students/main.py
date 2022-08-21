


def main():
    student = get_students()
    print(f"{student[0]} is from {student[1]}")


def get_students():
   name = input("Name: ")
   house = input("House: ")
   return name, house



if __name__ == "__main__":
    main()