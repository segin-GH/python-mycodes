def main():
    student = get_students()
    print(f"{student['name']} is from {student['house']}")


def get_students():
    student = {}
    student["name"] = input("name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()
