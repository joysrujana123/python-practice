students = []
marks = []

def add_student():
    name = input("Enter student name: ")
    mark = float(input("Enter marks: "))
    
    students.append(name)
    marks.append(mark)
    
    print("Student added!")

def view_students():
    if not students:
        print("No students added yet.")
        return
    
    print("\nStudent List")
    for i in range(len(students)):
        print(students[i], "-", marks[i])

def average_marks():
    if not marks:
        print("No marks available.")
        return
    
    avg = sum(marks) / len(marks)
    print("Average Marks:", avg)


while True:
    print("\nStudent Marks Manager")
    print("1 Add Student")
    print("2 View Students")
    print("3 Average Marks")
    print("4 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        average_marks()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
