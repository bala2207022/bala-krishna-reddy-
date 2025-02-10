import random

letters = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("1234567890")
symbols = ["@", "$", "&"]

print("Welcome to Password Generator ")

a = int(input("Enter how many letters you want: "))
b = int(input("Enter how many numbers you want: "))
c = input("Choose one symbol (@, $, &): ")

if c in symbols:
    password = ""

    for _ in range(a):
        password += random.choice(letters)

    password += c

    for _ in range(b):
        password += random.choice(numbers)

    print("Generated Password: " + password)

else:
    print("Error: Invalid symbol selected! Please choose from @, $, &.")
