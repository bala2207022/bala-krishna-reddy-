num1 = float(input("ENTER YOU NUMBER = "))
num2 = float(input("enter your number = "))
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

if choice == '1':
            print(f"The result of addition is: {num1 + num2}")
elif choice == '2':
            print(f"The result of subtraction is: {num1 - num2}")
elif choice == '3':
            print(f"The result of multiplication is: {num1 * num2}")
elif choice == '4':
            # Handle division by zero
    if num2 != 0:
                print(f"The result of division is: {num1 / num2}")
    else:
                print("Error: Division by zero is not allowed.")
else:
        print("Invalid input! Please select a valid operation.")
