a=[]
with open("Students.txt", "r") as f:
    for line in f:
        name, sid = line.strip().split(",")
        a.append([name, int(sid)])
while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    print("4. Search Student")
    print("5.Delete Student")
    print("6.Update Student:")
    print("7.Total Students:")
    c=int(input("Enter Your Choice:"))
    if c==1:
        print("Add Student")
        s=input("Enter name:")
        sid=int(input("Enter id:"))
        f=False
        for i in a:
            if i[1]==sid:
                f=True
                break
        if f:
            print("ID already exists")
        else:
            a.append([s,sid])
            with open("Students.txt","a") as f:
                f.write(f"{s},{sid}\n")
    elif c==2:
        print("View Students")
        for i in a:
            print("Name:",i[0])
            print("ID:",i[1])
    elif c==3:
        print("Exit")
        break
    elif c==4:
        sid=int(input("Enter ID to search:"))
        f=False
        for i in a:
            if i[1]==sid:
                 print("Student Found")
                 print("Name:",i[0])
                 print("ID:",i[1])
                 f=True
                 break
        if not f:
             print("Student Not Found")
    elif c==5:
        sid=int(input("Enter ID to delete student Record:"))
        f=False
        for i in range(len(a)):
            if a[i][1]==sid:
                a.pop(i)
                print("Deleted Succesfully")
                with open("Students.txt", "w") as f:
                    for student in a:
                        f.write(f"{student[0]},{student[1]}\n")
                f=True
                break
        if not f:
            print("Student not found")
    elif c==6:
        sid=int(input("Enter ID to Update:"))
        ai=input("Enter Update Name:")
        f=False
        for i in a:
            if i[1]==sid:
                i[0]=ai
                print("Updated Succesfully")
                with open("Students.txt", "w") as f:
                    for student in a:
                        f.write(f"{student[0]},{student[1]}\n")
                f=True
                break
        if not f:
            print("Student id not found:")
    elif c==7:
        print("Total Students:", len(a))
