class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing Name")
        # if house not in ["gryffindor","hufflepuff","ravenclaw","slytherin"]:
        #     raise ValueError("Invalid House")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is from {self.house}"


def main():
    student = get_student()
    print(student)
    # print(f"{student.name} is from {student.house}")


def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
