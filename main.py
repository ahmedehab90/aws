students = []

def main():
    x = input("Enter the number of students: ")
    i = 0
    while i < int(x):
        x1 = input("Enter the student's name: ")
        x2 = input("Enter the student's age: ")
        x3 = input("Enter the student's gender: ")
        x4 = input("Enter the student's location: ")
        x5 = input("Enter the student's grade: ")
        x6 = input("Enter the student's cell number: ")
        print("##########################")
        inputs(x1, int(x2), x3, x4, int(x5), x6)
        i = i + 1

def inputs(name, age, gender, loc, grade, cell):
    students.append({"name": name, "age": age, "gender": gender, "loc": loc, "grade": grade, "cell": cell})

def showStudent(y,rx = False):
    if checkYes(y):
        x = findStudent(input("Enter the name of the student: "))
        if x != "not found" :
            printStudents(x)
        if rx:
            return x

def findStudent(name):
    for i in students:
        if i["name"] == name:
            return i
        else:
            return "not found"

def printStudents(x):
    print("his name is " + x["name"])
    print("his age is " + str(x["age"]))
    print("his gender is " + x["gender"])
    print("his location is " + x["loc"])
    print("his grade is " + str(x["grade"]))
    print("his cell number is " + x["cell"])

def checkYes(y):
    return True if y.lower() == "yes" else False

def editStudent(y):
    if checkYes(y):
        x = showStudent(y, True)
        e = input("What to edit: ")
        value = input("you want edit "+ e +" to ")
        if e == "name":
            x["name"] = value
        elif e == "age":
            x["age"] = int(value)
        elif e == "gender":
            x["gender"] == value
        elif e == "location":
            x["loc"] == value
        elif e == "grade":
            x["grade"] == int(value)
        else:
            x["cell"] == value
        printStudents(x)

def deleteStudent(y):
    if checkYes(y):
        i = findStudent(input("enter the name of the student: "))
        x = 0
        while x < len(students):
            if students[x] == i:
                students[x].remove()
    print("done")

def studentsInFile(y):
    if checkYes(y):
        f = open("students.txt","a")
        x = 0
        for i in students:
            f.write(str(x+1) + ")student name is " + i["name"]+'\n')
            f.write(str(x+1) + ")student age is " + str(i["age"])+'\n')
            f.write(str(x+1) + ")student gender is " + i["gender"]+'\n')
            f.write(str(x+1) + ")student location is " + i["loc"]+'\n')
            f.write(str(x+1) + ")student grade is " + str(i["grade"])+'\n')
            f.write(str(x+1) + ")student cell number is " + i["cell"]+'\n')
            f.write("##########################################")
            x = x + 1
    print("done")

main()
showStudent(input("do you want to show student? "))
editStudent(input("do you want to edit student's data? "))
deleteStudent(input("do you want to delete a student? "))
studentsInFile(input("do you want to print the data in a file? "))