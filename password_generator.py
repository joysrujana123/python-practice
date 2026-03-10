import random
import string

while True:
    print("\nPassword Generator")
    print("1 Generate password")
    print("2 Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        length = int(input("Enter password length: "))

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
