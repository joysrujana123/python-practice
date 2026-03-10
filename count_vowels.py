text = input("Enter a string: ")

count = 0
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
