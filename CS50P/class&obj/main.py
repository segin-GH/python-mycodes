
class Student:

    def __init__(self, name, house, pet):
        if not name:
            raise ValueError("Missing Name")
        # if house not in ["gryffindor","hufflepuff","ravenclaw","slytherin"]:
        #     raise ValueError("Invalid House")
        self.name = name
        self.house = house 
        self.pet = pet


    def __str__(self):
        return f"{self.name} is from {self.house}"


    def charm(self):

        match self.pet:
            case "stag":
                return "bbbb"
            case "otter":
                return "mmmm"
            case _:
                return "......"



def main():
    student = get_student()
    print(student)
    print(student.charm())
    # print(f"{student.name} is from {student.house}")



def get_student():
    name = input("name: ")
    house = input("house: ")
    pet = input("patronus: ")
    return Student(name,house,pet) 
    
    


if __name__ == "__main__":
    main()


