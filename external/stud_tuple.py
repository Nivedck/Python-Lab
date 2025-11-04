students=[]

# Do the Empolyee Question with the same idea , with tupls

def add_student():
    stud_id =int(input("Enter Student ID:"))
    name = input("Enter Student Name:")
    age = int(input("Enter Student Age:"))
    adm_no =input("Enter Admission Number (Eg: 2024B999) :")

    stud_tuple = (stud_id,name,age,adm_no)
    students.append(stud_tuple)


def delete_student(stud_id):
    found = False
    for i in students:
        if(i[0]==stud_id):
            found=True
            students.remove(i)
            print("Removed Student ✅️")

    if(found==False):
        print("No Student ")

def search_student(stud_id):
    found=False
    for i in students:
        if(i[0]==stud_id):
            found=True
            print()
            print("Name:",i[1])
            print("Age:",i[2])
            print("Admission Number:",i[3])
            print()

    if found == False:
        print("Student Not Found!")
        print()


while True:
    print("----- Student Management -----")
    print()
    print("1.Add Student")
    print("2.Delete Student")
    print("3.Search Student")
    print("4.Exit")

    print()
    choice = int(input("Enter a choice:"))

    match choice:
        case 1:
            add_student()
        case 2:
            delete_student(int(input("Enter Student ID:")))
        case 3:
            search_student(int(input("Enter Student ID:")))
        case 4:
            break
        case _:
            print("Enter a valid choice!")


