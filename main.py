from calculator import calculator
from to_do_manager import todo
from password_generator import generate_password

while True:
    print("\nStudent Productivity Toolkit")
    print("1. Calculator")
    print("2. To Do Manager")
    print("3. Password Generator")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo()

    elif choice == "3":
        generate_password()

    elif choice == "4":
        break
