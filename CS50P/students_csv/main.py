

# main function
def main():
    
    # list of students
    students = []
    # opened a file called "students.csv"
    with open("students.csv") as file:
    # iterating through each line
        for line in file:
            # initalizing two var 
            # stiping of "\n" from line, sliting after ","
            name, house = line.rstrip().split(",")
            # making a dictionary of student addin key like name and house
            student = {"name" : name, "house" : house}
            # adding student dictonary to students
            students.append(student)
 
    #function that prints the students
    printStudents(students)

# a function that returns student["name"]
def get_name(student):
    return student["name"]

# a function that prints all the students sorted
def printStudents(students):
    for student in sorted(students,key= get_name):
        print(f"{student['name']} is in {student['house']}.")




if __name__ == "__main__":
    main()

