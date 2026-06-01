import random
import string

length = int(input("Enter password length: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

password = []

# guarantee one of each
password.append(random.choice(letters))
password.append(random.choice(digits))
password.append(random.choice(symbols))

all_characters = letters + digits + symbols

for i in range(length - 3):
    password.append(random.choice(all_characters))

random.shuffle(password)

final_password = "".join(password)

print("Generated Password:", final_password)
