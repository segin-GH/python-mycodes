


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house 



def main():
    student = get_student()
    print(f"{student.name} is from {student.house}")



def get_student():
    name = input("name: ")
    house = input("house: ")
    student = Student(name,house)
    return student 
    


if __name__ == "__main__":
    main()



    # student = Student
    # student.name = input("Name: ")
    # student.house = input("House: ")
    # return student