tasks = []

while True:
    print("\nTo-Do List Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(i, "-", task)

    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        tasks.pop(num-1)
        print("Task removed!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
